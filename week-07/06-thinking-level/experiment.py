LEVELS = ["minimal", "low", "medium", "high"]
OBSERVATIONS = {"minimal":"short direct answer","low":"brief rationale","medium":"structured reasoning","high":"deeper checks and alternatives"}
def matrix(): return [{"level": level, "observation": OBSERVATIONS[level]} for level in LEVELS]
def run(client, prompt): return [{"level": level, "output": client.generate(prompt, thinking_level=level)} for level in LEVELS]
