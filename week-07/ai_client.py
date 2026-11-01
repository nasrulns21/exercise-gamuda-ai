import json, os, urllib.request

class FixtureAIClient:
    def __init__(self, response="Sample response"): self.response = response
    def generate(self, prompt, **options): return self.response

class GeminiAIClient:
    def __init__(self, api_key=None, model="gemini-2.5-flash"):
        self.api_key = api_key or os.environ["GEMINI_API_KEY"]; self.model = model
    def generate(self, prompt, **options):
        url=f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={self.api_key}"
        body={"contents":[{"parts":[{"text":prompt}]}],"generationConfig":options}
        request=urllib.request.Request(url,data=json.dumps(body).encode(),headers={"Content-Type":"application/json"})
        with urllib.request.urlopen(request,timeout=30) as response: data=json.load(response)
        return data["candidates"][0]["content"]["parts"][0]["text"]
