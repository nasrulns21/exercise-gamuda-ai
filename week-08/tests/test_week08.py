import importlib.util
from pathlib import Path
import pytest

ROOT = Path(__file__).parents[1]
def load(folder):
    spec = importlib.util.spec_from_file_location(folder, ROOT / folder / "prompts.py")
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module); return module

def test_image_prompt_is_customisable_and_validated():
    m = load("01-image-analytics")
    result = m.build_image_request("site.jpg", "image/jpeg", "Inspect PPE compliance")
    assert result["prompt"] == "Inspect PPE compliance"
    with pytest.raises(ValueError): m.build_image_request("file.pdf", "application/pdf", "Inspect")
    with pytest.raises(ValueError): m.build_image_request("site.jpg", "image/jpeg", " ")

def test_video_has_all_required_output_modes():
    m = load("02-video-analytics")
    assert set(m.PROMPTS) == {"detailed", "bullets", "timecoded", "quiz"}
    assert "[MM:SS]" in m.build_video_request("training.mp4", "timecoded")["prompt"]
    assert "answer key" in m.build_video_request("training.mp4", "quiz")["prompt"].lower()
