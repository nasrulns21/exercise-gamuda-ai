PROMPTS = {
 "detailed": "Provide a detailed chronological summary including people, actions, setting, and important changes.",
 "bullets": "Summarise the video as concise bullet points in chronological order.",
 "timecoded": "Write chronological paragraphs. Start every paragraph with an estimated [MM:SS] timestamp.",
 "quiz": "Create five comprehension questions followed by a clearly separated answer key.",
}

def build_video_request(filename: str, mode: str):
    if mode not in PROMPTS: raise ValueError("Unknown analysis mode")
    return {"filename": filename, "mode": mode, "prompt": PROMPTS[mode]}
