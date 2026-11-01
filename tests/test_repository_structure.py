from pathlib import Path
import json
import subprocess


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_IDS = [
    *(f"W01-E{i:02d}" for i in range(1, 5)),
    *(f"W02-E{i:02d}" for i in range(1, 12)),
    "W03-E01",
    *(f"W04-E{i:02d}" for i in range(1, 11)),
    *(f"W05-E{i:02d}" for i in range(1, 11)),
    *(f"W06-E{i:02d}" for i in range(1, 5)),
    *(f"W07-E{i:02d}" for i in range(1, 9)),
    *(f"W08-E{i:02d}" for i in range(1, 3)),
]


def test_coverage_ledger_lists_every_exercise_once():
    ledger = (ROOT / "EXERCISE-COVERAGE.md").read_text(encoding="utf-8")
    for exercise_id in EXPECTED_IDS:
        assert ledger.count(f"| {exercise_id} |") == 1, exercise_id


def test_interim_coverage_uses_only_valid_statuses():
    ledger = (ROOT / "EXERCISE-COVERAGE.md").read_text(encoding="utf-8")
    rows = [line for line in ledger.splitlines() if line.startswith("| W")]
    assert len(rows) == len(EXPECTED_IDS)
    valid = {"Planned", "Complete", "External verification required", "Not applicable duplicate"}
    for row in rows:
        assert row.split("|")[4].strip() in valid, row


def test_final_coverage_has_no_planned_exercises():
    ledger = (ROOT / "EXERCISE-COVERAGE.md").read_text(encoding="utf-8")
    rows = [line for line in ledger.splitlines() if line.startswith("| W")]
    assert all("| Planned |" not in row for row in rows)


def test_root_node_harness_exposes_repeatable_commands():
    package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
    scripts = package["scripts"]
    assert {"test", "test:repository", "test:browser", "verify"} <= scripts.keys()


def test_gitignore_blocks_generated_and_secret_files():
    ignored = (ROOT / ".gitignore").read_text(encoding="utf-8")
    for rule in (".env", "node_modules/", "dist/", "__pycache__/", ".pytest_cache/"):
        assert rule in ignored


def test_repository_has_no_zero_byte_tracked_content():
    names = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout.splitlines()
    empty = [Path(name) for name in names if (ROOT / name).stat().st_size == 0]
    assert empty == []
