
import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser

# Load API key daripada Week 7/.env
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# Setup Gemini AI
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# Enable URL context
llm_with_url = llm.bind_tools([{"url_context": {}}])

# Website to summarize
URL = "https://blog.google/technology/ai/google-gemini-ai"

# Create chain
chain = llm_with_url | StrOutputParser()

# Ask AI to summarize webpage
response = chain.invoke([
    HumanMessage(
        content=f"Write a concise summary of this page: {URL}"
    )
])

# Display result
print(response)
