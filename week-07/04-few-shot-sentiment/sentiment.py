EXAMPLES = [("The workshop was excellent", "positive"), ("The app keeps crashing", "negative"), ("The meeting is at noon", "neutral"), ("Support solved it quickly", "positive"), ("The instructions are unclear", "negative")]
def prompt(text):
    shots = "\n".join(f"Text: {sample}\nSentiment: {label}" for sample, label in EXAMPLES)
    return f"Classify as positive, negative, or neutral.\n{shots}\nText: {text}\nSentiment:"
def classify(client, text): return client.generate(prompt(text)).strip().lower()
