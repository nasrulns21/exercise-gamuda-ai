
import os
from pathlib import Path
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

# 1. Load API key from Week 7/.env
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

# 2. Setup Gemini AI
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=api_key
)

# 3. Create prompt with conversation history
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful assistant. "
        "Answer all questions to the best of your ability."
    ),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

# 4. Create LangChain
chain = prompt | llm | StrOutputParser()

# 5. Store conversation history
history = []

print("\nStarting chat... Type 'quit' or 'exit' to end.")

# 6. Start conversation
while True:
    user_input = input("You: ")

    if user_input.lower().strip() in ["quit", "exit"]:
        break

    if not user_input.strip():
        print("Please enter a message.")
        continue

    try:
        response = chain.invoke({
            "input": user_input,
            "history": history
        })

        history.append(HumanMessage(content=user_input))
        history.append(AIMessage(content=response))

        print(f"AI: {response}")

    except Exception as e:
        print(f"An error occurred: {e}")

print("\nChat ended.")
