import importlib.util
from pathlib import Path
import pytest
from pydantic import ValidationError

ROOT = Path(__file__).parents[1]
def load(folder, file):
    spec = importlib.util.spec_from_file_location(folder, ROOT / folder / file)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module); return module

def test_translation_validation_and_prompt():
    m = load("01-translation-api/backend", "app/main.py")
    request = m.TranslationRequest(text="Good morning", target_language="Malay")
    assert m.fixture_translate(request).translated_text == "Selamat pagi"
    assert "Malay" in m.build_prompt(request)
    with pytest.raises(ValidationError): m.TranslationRequest(text="", target_language="M")

def test_temperature_and_roles():
    temp = load("02-temperature-experiment", "experiment.py")
    roles = load("03-system-role-experiment", "experiment.py")
    assert [x["temperature"] for x in temp.experiment_matrix()] == [0.0, .5, 1.0, 1.5, 2.0]
    assert {"tone", "detail", "complexity", "information"} <= set(roles.ROLES["teacher"])

def test_few_shot_and_json_parser():
    sentiment = load("04-few-shot-sentiment", "sentiment.py")
    parser = load("05-json-output-parser", "parser.py")
    assert len(sentiment.EXAMPLES) >= 5
    assert parser.parse_output('{"topic":"Python","priority":3,"reason":"Useful"}').priority == 3
    with pytest.raises(Exception): parser.parse_output('{"topic":"Python","priority":9,"reason":"No"}')

def test_thinking_document_and_webpage_variants():
    thinking = load("06-thinking-level", "experiment.py")
    docs = load("07-document-summarisation", "prompts.py")
    web = load("08-webpage-summarisation", "prompts.py")
    assert [x["level"] for x in thinking.matrix()] == ["minimal", "low", "medium", "high"]
    assert len(docs.FORMATS) == 3 and "limitations" in docs.build_prompt("technical", "text")
    assert set(web.FORMATS) == {"bullets", "takeaways", "qa"}
