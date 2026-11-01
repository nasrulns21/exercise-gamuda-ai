
import os
from io import BytesIO
from pathlib import Path

from pypdf import PdfReader
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, HTTPException

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Setup FastAPI
app = FastAPI(title="PDF Text Summarization")

# 2. Load API key from Week 7/.env
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

# 3. Setup Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=api_key
)

# 4. Create Prompt Template
prompt_template = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful assistant that summarizes documents."
    ),
    (
        "human",
        "Write a concise summary of the following:\n\n"
        "{text}\n\nCONCISE SUMMARY:"
    )
])

# 5. Create Chain
chain = prompt_template | llm | StrOutputParser()

# 6. Read PDF contents
def read_pdf_file(file_contents: BytesIO) -> str:
    try:
        pdf_reader = PdfReader(file_contents)

        return "\n".join(
            page.extract_text() or ""
            for page in pdf_reader.pages
        )

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Error reading PDF file."
        )


# 7. Create API endpoint
@app.post("/summarize")
async def summarize_pdf(file: UploadFile = File(...)):

    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    contents = await file.read()

    # Limit PDF size to 10 MB
    if len(contents) > 10 * 1024 * 1024:
        raise HTTPException(
            status_code=413,
            detail="PDF file is too large."
        )

    text = read_pdf_file(BytesIO(contents))

    if not text.strip():
        raise HTTPException(
            status_code=400,
            detail="No readable text found."
        )

    try:
        summary = await chain.ainvoke({"text": text})

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="An error occurred while summarizing the document."
        )

    return {"summary": summary}

