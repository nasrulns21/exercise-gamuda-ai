ROLES = {
 "teacher": {"tone": "supportive", "detail": "step-by-step", "complexity": "beginner", "information": "examples"},
 "engineer": {"tone": "precise", "detail": "implementation", "complexity": "technical", "information": "constraints"},
 "executive": {"tone": "concise", "detail": "summary", "complexity": "strategic", "information": "decisions"},
}
def role_prompt(role, question): return f"You are a {role}. Answer with the expected tone and detail.\nQuestion: {question}"
def run(client, question): return {role: client.generate(role_prompt(role, question)) for role in ROLES}
