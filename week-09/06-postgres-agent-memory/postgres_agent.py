import os

from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.postgres import PostgresSaver

from settings import database_uri


def run_conversation(thread_id: str = "nasrul-training") -> str:
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.environ["GEMINI_API_KEY"])
    with PostgresSaver.from_conn_string(database_uri()) as checkpointer:
        checkpointer.setup()
        agent = create_agent(model=model, tools=[], checkpointer=checkpointer)
        config = {"configurable": {"thread_id": thread_id}}
        result = agent.invoke({"messages": [{"role": "user", "content": "Remember that my project is a RAG chatbot."}]}, config)
        return result["messages"][-1].text


if __name__ == "__main__":
    print(run_conversation())
