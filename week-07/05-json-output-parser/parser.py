import json
from pydantic import BaseModel, Field

class TrainingRecommendation(BaseModel):
    topic: str = Field(min_length=1)
    priority: int = Field(ge=1, le=5)
    reason: str = Field(min_length=1)

def prompt(profile): return f'Recommend training for {profile}. Return JSON with topic, priority (1-5), and reason.'
def parse_output(value): return TrainingRecommendation.model_validate(json.loads(value))
def run(client, profile): return parse_output(client.generate(prompt(profile)))
