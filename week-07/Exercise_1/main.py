from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
from pathlib import Path
import os

# Load .env dari folder Week 7
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

app = FastAPI(title="Exercise 1 - Translation API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

# Request body
class TranslationRequest(BaseModel):
    input_language: str
    output_language: str
    text_input: str


@app.get("/")
def home():
    return {"message": "Translation API is running!"}


@app.post("/translate")
def translate_text(request: TranslationRequest):

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="GEMINI_API_KEY not found in .env"
        )

    try:
        client = genai.Client(api_key=api_key)

        prompt = f"""
        Translate the following text from
        {request.input_language} to
        {request.output_language}.

        Return only the translated text.

        Text: {request.text_input}
        """

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        if not response.text:
            raise ValueError("Empty translation response")

        return {
            "translated_text": response.text.strip()
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Translation failed: {str(e)}"
        )
