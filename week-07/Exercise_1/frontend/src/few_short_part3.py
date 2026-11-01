
import os
from dotenv import load_dotenv
from langchain_core.prompts import (
    FewShotPromptTemplate,
    PromptTemplate
)
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. Load API Key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

# 2. Setup Gemini AI
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=api_key,
    
)

# 3. Few-Shot Examples
examples = [
    {
        "review": "This coffee tastes amazing!",
        "sentiment": "Positive"
    },
    {
        "review": "The coffee is terrible and bitter.",
        "sentiment": "Negative"
    },
    {
        "review": "Great aroma but too expensive.",
        "sentiment": "Mixed"
    },
    {
        "review": "I bought coffee this morning.",
        "sentiment": "Neutral"
    }
]

# 4. Example Prompt Template
example_prompt = PromptTemplate(
    input_variables=["review", "sentiment"],
    template="Coffee Review: {review}\nSentiment: {sentiment}"
)

# 5. Few-Shot Prompt Template
prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix=(
        "Analyze the coffee review sentiment.\n"
        "Respond with ONLY ONE WORD: "
        "Positive, Negative, Mixed, or Neutral.\n"
    ),
    suffix="Coffee Review: {input}\nSentiment:",
    input_variables=["input"]
)

# 6. Create LangChain
chain = prompt | llm | StrOutputParser()

# 7. User Input Loop
print("Coffee Review Sentiment Analyzer (type 'quit' to exit)")

while True:
    review = input("Enter coffee review: ").strip()

    if not review:
        continue

    if review.lower() == "quit":
        break

    try:
        response = chain.invoke({"input": review})
        print(response.strip())

    except Exception as e:
        print(f"Error: {e}")

print("\nProgram ended.")
