import asyncio
import os

from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters.client import MultiServerMCPClient

from servers import build_servers


async def main():
    if not os.getenv("TAVILY_API_KEY"):
        raise SystemExit("TAVILY_API_KEY is missing")
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.environ["GEMINI_API_KEY"])
    client = MultiServerMCPClient(build_servers())
    tools = await client.get_tools()
    print("Tools available:", [tool.name for tool in tools])
    agent = create_agent(model=model, tools=tools, system_prompt="Use tools when current or calculated information is required.")
    result = await agent.ainvoke({"messages": [{"role": "user", "content": "Find a current Malaysia technology headline, then give me a random number from 1 to 10."}]})
    used = [message.name for message in result["messages"] if message.type == "tool"]
    print("Tools used:", used)
    print(result["messages"][-1].text)


if __name__ == "__main__":
    asyncio.run(main())
