from langchain_openai import ChatOpenAI
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from dotenv import load_dotenv

load_dotenv()

store = {}

llm = ChatOpenAI(
    model="gpt-4o-mini",
)

messages = [
    (
        "system",
        "Eres un asistente que sabe mucho de anime y manga, te encanta hablar de ello.",
    ),
    MessagesPlaceholder(variable_name="history"),
    (
        "user",
        "{input}",
    ),
]

prompt = ChatPromptTemplate.from_messages(messages)
runnable = prompt | llm


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


with_message_history = RunnableWithMessageHistory(
    runnable,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

message = with_message_history.invoke(
    {"input": "Dime una frase famosa de Death Note"}, config={"session_id": "1"}
)

print(message)

message = with_message_history.invoke(
    {"input": "Repite lo último en ingles"}, config={"session_id": "1"}
)

print(message)
