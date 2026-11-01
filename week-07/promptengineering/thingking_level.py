
import os
from pathlib import Path
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Load API key from Week 7/.env
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# 2. Set thinking level
THINKING_LEVEL = "low"

# 3. Setup Gemini AI
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    thinking_level=THINKING_LEVEL
)

# 4. Create prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{question}")
])

# 5. Create chain
chain = prompt | llm | StrOutputParser()

# 6. Ask question
response = chain.invoke({
    "question": "Provide a list of 3 famous physicists and their key contributions."
})

# 7. Print result
print(f"Thinking Level : {THINKING_LEVEL}")
print(f"Response       : \n{response}")
