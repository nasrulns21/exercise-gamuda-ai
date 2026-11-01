
import os
from pathlib import Path
from dotenv import load_dotenv

from langchain_core.prompts import (
    FewShotPromptTemplate,
    PromptTemplate
)
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. Load API key from Week 7/.env
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

# 2. Setup Gemini AI
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=api_key
)

# 3. Few-Shot Examples (8 examples)
examples = [
    {
        "review": "The mechanic fixed my car perfectly!",
        "sentiment": "Positive"
    },
    {
        "review": "Excellent service and very friendly staff.",
        "sentiment": "Positive"
    },
    {
        "review": "My car still has the same problem.",
        "sentiment": "Negative"
    },
    {
        "review": "Terrible service and unprofessional mechanic.",
        "sentiment": "Negative"
    },
    {
        "review": "Good repair but the price was too high.",
        "sentiment": "Mixed"
    },
    {
        "review": "Friendly staff but the service was very slow.",
        "sentiment": "Mixed"
    },
    {
        "review": "I sent my car for servicing today.",
        "sentiment": "Neutral"
    },
    {
        "review": "The workshop opens at 9 AM.",
        "sentiment": "Neutral"
    }
]

# 4. Create example prompt
example_prompt = PromptTemplate(
    input_variables=["review", "sentiment"],
    template="Customer Review: {review}\nSentiment: {sentiment}"
)

# 5. Create Few-Shot Prompt Template
prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix=(
        "Analyze customer reviews about automotive workshops.\n"
        "Classify each review based on its sentiment.\n"
        "Respond with ONLY ONE WORD: "
        "Positive, Negative, Mixed, or Neutral.\n"
    ),
    suffix="Customer Review: {input}\nSentiment:",
    input_variables=["input"]
)

# 6. Create LangChain
chain = prompt | llm | StrOutputParser()

# 7. User input loop
print("Automotive Customer Review Sentiment Analyzer")
print("Type 'quit' to exit.\n")

while True:
    review = input("Enter customer review: ").strip()

    if review.lower() == "quit":
        break

    if not review:
        continue

    try:
        response = chain.invoke({"input": review})
        print("Sentiment:", response.strip())
        print()

    except Exception as e:
        print(f"Error: {e}")

print("\nProgram ended.")
