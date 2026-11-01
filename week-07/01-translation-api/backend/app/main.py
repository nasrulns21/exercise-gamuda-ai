from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import sys
import os
sys.path.insert(0, str(Path(__file__).parents[3]))
from ai_client import FixtureAIClient, GeminiAIClient
from pydantic import BaseModel, Field

class TranslationRequest(BaseModel):
    text: str = Field(min_length=1, max_length=2000)
    target_language: str = Field(min_length=2, max_length=40)

class TranslationResponse(BaseModel):
    translated_text: str
    target_language: str

def build_prompt(request: TranslationRequest):
    return f"Translate into {request.target_language}. Return only the translation:\n{request.text}"

def fixture_translate(request: TranslationRequest):
    samples = {("Good morning", "Malay"): "Selamat pagi"}
    return TranslationResponse(translated_text=samples.get((request.text, request.target_language), f"[{request.target_language}] {request.text}"), target_language=request.target_language)

def translate_with(request, client):
    return TranslationResponse(translated_text=client.generate(build_prompt(request)).strip(), target_language=request.target_language)

app = FastAPI(title="Translation API")
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173"], allow_methods=["*"], allow_headers=["*"])
@app.post("/translate", response_model=TranslationResponse)
async def translate(request: TranslationRequest):
    if os.getenv("GEMINI_API_KEY"):
        return translate_with(request, GeminiAIClient())
    return fixture_translate(request)
