ALLOWED_TYPES = {"image/jpeg", "image/png", "image/webp"}

def build_image_request(filename: str, mime_type: str, prompt: str):
    if mime_type not in ALLOWED_TYPES: raise ValueError("Unsupported image type")
    if not prompt.strip(): raise ValueError("Prompt is required")
    return {"filename": filename, "mime_type": mime_type, "prompt": prompt.strip()}
