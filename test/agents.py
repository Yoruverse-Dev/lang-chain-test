from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

search = TavilySearchResults()

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Soy un asistente que sabe mucho de criptomonedas, puedo darte información sobre precios de criptomonedas.",
        ),
        ("user", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)
tools = [search]

agent = create_tool_calling_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

message = executor.invoke({"input": "Cuál es el precio de SCPT en USD?"})

print(message)
