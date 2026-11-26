from collections.abc import Callable


def generate_with_fallback(prompt: str, models: list[Callable[[str], str]]) -> str:
    if not models:
        raise ValueError("At least one model is required")
    last_error = None
    for model in models:
        try:
            return model(prompt)
        except Exception as error:
            last_error = error
    raise RuntimeError("All configured models failed") from last_error
