
import os
import ast
import json
import math
import operator
from pathlib import Path

from dotenv import load_dotenv
from tavily import TavilyClient
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# 1. Load API keys
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not GEMINI_API_KEY or not TAVILY_API_KEY:
    raise ValueError("Check GEMINI_API_KEY and TAVILY_API_KEY in .env")

# 2. Setup Tavily and Gemini
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=GEMINI_API_KEY
)

# 3. Safe mathematical calculator
ops = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

def calculate(node):
    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        if abs(node.value) > 1e10:
            raise ValueError("Number too large")
        return node.value

    if isinstance(node, ast.UnaryOp) and type(node.op) in ops:
        return ops[type(node.op)](calculate(node.operand))

    if isinstance(node, ast.BinOp) and type(node.op) in ops:
        left = calculate(node.left)
        right = calculate(node.right)

        if isinstance(node.op, ast.Pow):
            if abs(left) > 1e6 or abs(right) > 20:
                raise ValueError("Power too large")

        result = ops[type(node.op)](left, right)
        if not math.isfinite(result) or abs(result) > 1e15:
            raise ValueError("Result too large")
        return result

    raise ValueError("Unsupported expression")


# 4. Calculator Tool
@tool("calculator")
def tool1(expression: str) -> str:
    """Perform basic mathematical calculations."""
    try:
        tree = ast.parse(expression, mode="eval")

        if len(list(ast.walk(tree))) > 50:
            raise ValueError("Expression too complex")

        result = calculate(tree.body)
        return str(result)
    except Exception as e:
        return f"Calculator error: {e}"


# 5. Tavily Web Search Tool
@tool("web_search")
def tool2(query: str) -> str:
    """Search the web for information and source URLs."""
    try:
        result = tavily_client.search(
            query=query,
            search_depth="basic",
            max_results=5
        )

        sources = [
            {
                "title": item.get("title"),
                "url": item.get("url"),
                "content": item.get("content", "")[:1000]
            }
            for item in result.get("results", [])
        ]

        return json.dumps(sources, ensure_ascii=False)

    except Exception as e:
        return f"Web search error: {e}"


# 6. Create AI Agent with 2 tools
tools = [tool1, tool2]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=(
        "You are a helpful AI assistant. "
        "Use calculator for calculations and web_search "
        "for online information. "
        "Cite source URLs when using web search. "
        "Do not invent facts or missing information. "
        "For halal certificate enquiries, never claim "
        "a certificate is valid, expired, suspended or "
        "revoked unless official evidence confirms it. "
        "Refer users to https://www.halal.gov.my/ "
        "when verification is inconclusive."
    )
)

# 7. Ask user a question
print("AI Agent with Calculator + Tavily")
print("Type 'quit' to exit.")

while True:
    user_input = input("\nQuestion: ").strip()

    if user_input.lower() == "quit":
        break

    if not user_input:
        continue

    try:
        response = agent.invoke({
            "messages": [
                HumanMessage(content=user_input)
            ]
        })

        # Show which tools were called
        for message in response["messages"]:
            for call in getattr(message, "tool_calls", []):
                print("\nTool called:", call["name"])
                print("Arguments:", call["args"])

        final_message = response["messages"][-1]

        print("\nAI Answer:")
        print(final_message.text)

    except Exception as e:
        print(f"Error: {e}")

print("\nProgram ended.")
