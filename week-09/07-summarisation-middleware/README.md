# Summarisation Middleware

Long conversations are compacted by replacing older messages with a summary while keeping the newest messages unchanged. The pure Python version makes the behaviour easy to inspect before connecting it to LangChain middleware.

Observation: the agent retains the main topic and recent details while using fewer messages. Very aggressive summarisation can remove small facts, so the number of recent messages should match the task.
