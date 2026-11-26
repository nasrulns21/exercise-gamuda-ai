# Model Fallback

Attempts the primary model first and moves through configured alternatives only when a call fails. This pattern keeps an agent usable during a temporary model outage.

Observation: the first successful model returns the answer. If every model fails, the last error is raised so the application can report the failure clearly.
