from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini",
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)
tool = WikipediaQueryRun(api_wrapper=api_wrapper)

message = tool.run("Shingeki no Kyojin")
print(message)
