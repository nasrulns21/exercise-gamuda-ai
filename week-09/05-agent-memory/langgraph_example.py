import os

from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver


def build_agent():
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.environ["GEMINI_API_KEY"])
    return create_agent(model=model, tools=[], checkpointer=InMemorySaver())


if __name__ == "__main__":
    agent = build_agent()
    config = {"configurable": {"thread_id": "training-thread"}}
    agent.invoke({"messages": [{"role": "user", "content": "My preferred language is Malay."}]}, config)
    result = agent.invoke({"messages": [{"role": "user", "content": "What language do I prefer?"}]}, config)
    print(result["messages"][-1].text)
