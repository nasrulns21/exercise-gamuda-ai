
import os
import ast
import math
import operator
from pathlib import Path

from dotenv import load_dotenv
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# 1. Load Gemini API Key
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

# 2. Setup Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    google_api_key=GEMINI_API_KEY
)

# 3. Safe calculator operators
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

def safe_calculate(node):
    if isinstance(node, ast.Constant):
        if type(node.value) in (int, float):
            if abs(node.value) > 1e12:
                raise ValueError("Number too large")
            return node.value

    if isinstance(node, ast.UnaryOp):
        if type(node.op) in OPERATORS:
            return OPERATORS[type(node.op)](
                safe_calculate(node.operand)
            )

    if isinstance(node, ast.BinOp):
        if type(node.op) in OPERATORS:
            left = safe_calculate(node.left)
            right = safe_calculate(node.right)

            if isinstance(node.op, ast.Pow):
                if abs(right) > 20 or abs(left) > 1e6:
                    raise ValueError("Power too large")

            result = OPERATORS[type(node.op)](left, right)

            if not math.isfinite(result) or abs(result) > 1e15:
                raise ValueError("Result too large")

            return result

    raise ValueError("Unsupported calculation")


# 4. Define Calculator Tool
@tool("calculator", description="Performs mathematical calculations.")
def tool1(expression: str) -> str:
    """Calculate a basic arithmetic expression safely."""
    try:
        tree = ast.parse(expression, mode="eval")
        result = safe_calculate(tree.body)
        return str(result)

    except Exception as e:
        return f"Error: {e}"


# 5. Create Agent
tools = [tool1]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=(
        "You are a helpful assistant. "
        "Use the calculator tool for mathematical calculations. "
        "For compound interest, assume annual compounding "
        "unless stated otherwise."
    )
)

# 6. User Question
question = HumanMessage(
    content=(
        "What's the result of an investment of "
        "$10,000 growing at 8% annually for "
        "5 years with compound interest?"
    )
)

# 7. Invoke Agent
print("AI Agent is calculating...\n")

response = agent.invoke({
    "messages": [question]
})

# 8. Display Tool Calls
for message in response["messages"]:
    if getattr(message, "tool_calls", None):
        for call in message.tool_calls:
            print("Tool called:", call["name"])
            print("Arguments:", call["args"])

# 9. Display Final Answer
final_message = response["messages"][-1]

print("\nFinal Answer:")
print(final_message.text)
