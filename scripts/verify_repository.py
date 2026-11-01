"""Repeatable repository-level checks for the training portfolio."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_PARTS = {"node_modules", "dist", "build", ".venv", "venv", "__pycache__", ".pytest_cache"}
SECRET_PATTERNS = (
    re.compile(r"AIza[0-9A-Za-z_-]{30,}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
)
LINK_PATTERN = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+)\)")


def tracked_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True
    )
    return [ROOT / name.decode("utf-8") for name in result.stdout.split(b"\0") if name]


def verify() -> list[str]:
    problems: list[str] = []
    files = tracked_files()
    for path in files:
        relative = path.relative_to(ROOT)
        if any(part in FORBIDDEN_PARTS for part in relative.parts):
            problems.append(f"forbidden tracked path: {relative}")
        if not path.exists():
            problems.append(f"missing tracked file: {relative}")
            continue
        if path.stat().st_size == 0:
            problems.append(f"zero-byte tracked file: {relative}")
        if path.stat().st_size > 5 * 1024 * 1024:
            problems.append(f"large tracked file over 5 MiB: {relative}")
        if path.suffix.lower() not in {".png", ".jpg", ".jpeg", ".gif", ".ico", ".pdf"}:
            text = path.read_text(encoding="utf-8", errors="ignore")
            for pattern in SECRET_PATTERNS:
                if pattern.search(text):
                    problems.append(f"credential-like value: {relative}")
            if path.suffix.lower() == ".md":
                for target in LINK_PATTERN.findall(text):
                    clean = target.split("#", 1)[0].replace("%20", " ")
                    if clean and not (path.parent / clean).resolve().exists():
                        problems.append(f"broken Markdown link in {relative}: {target}")
    return problems


if __name__ == "__main__":
    failures = verify()
    if failures:
        print("Repository verification failed:")
        print("\n".join(f"- {item}" for item in failures))
        raise SystemExit(1)
    print(f"Repository verification passed for {len(tracked_files())} tracked files.")
