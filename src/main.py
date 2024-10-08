# Load env variables
from dotenv import load_dotenv

load_dotenv()

# Prepare the DB
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


def prepare_db():
    CHROMA_PATH = "db"

    embedding = OpenAIEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding)

    print(f"Retrieved the DB from {CHROMA_PATH}.")

    return db


# Search in the DB
def search(query, db: Chroma):
    results = db.similarity_search_with_relevance_scores(query, k=5)

    if len(results) == 0 or results[0][1] < 0.7:
        print("No results found.")
        return

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])

    messages = [
        (
            "system",
            "Por favor, responde a la siguiente pregunta basándote únicamente en el contexto proporcionado: {context}",
        ),
        ("user", "{query}"),
    ]

    prompt = ChatPromptTemplate.from_messages(messages)

    llm = ChatOpenAI(
        model="gpt-4o-mini",
    )

    model = prompt | llm
    response_text = model.invoke({"context": context_text, "query": query})

    sources = [doc.metadata.get("source", None) for doc, _score in results]
    formatted_response = f"Response: {response_text.content}\n\nSources: {sources}"

    return formatted_response


db = prepare_db()

# Search for a query
query = 'Según el contrato de seguro ASISA Mascotas, ¿qué condición debe cumplir un perro clasificado como "potencialmente peligroso" para mantener la cobertura del seguro?'

response = search(query, db)

print(response)
