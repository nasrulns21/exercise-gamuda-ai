import os

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

from currency_tool import fetch_exchange_rate


@tool
def current_exchange_rate(base: str, quote: str) -> str:
    """Return the latest exchange rate for two three-letter currency codes."""
    result = fetch_exchange_rate(base, quote)
    return f"1 {result.base} = {result.rate} {result.quote} on {result.date}"


def build_agent():
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.environ["GEMINI_API_KEY"])
    return create_agent(model=model, tools=[current_exchange_rate], system_prompt="Use the exchange-rate tool for current currency questions.")


if __name__ == "__main__":
    agent = build_agent()
    result = agent.invoke({"messages": [{"role": "user", "content": "What is the current exchange rate from US dollars to Malaysian Ringgit?"}]})
    print(result["messages"][-1].text)
