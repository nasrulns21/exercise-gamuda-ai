TEMPERATURES = [0.0, 0.5, 1.0, 1.5, 2.0]
OBSERVATIONS = {
    0.0: "Most consistent and literal.", 0.5: "Mostly stable with mild variation.",
    1.0: "Balanced creativity and consistency.", 1.5: "More varied wording and ideas.",
    2.0: "Highest creativity with reduced predictability.",
}
def experiment_matrix(): return [{"temperature": value, "observation": OBSERVATIONS[value]} for value in TEMPERATURES]
def run(client, prompt): return [{"temperature": t, "output": client.generate(prompt, temperature=t)} for t in TEMPERATURES]
