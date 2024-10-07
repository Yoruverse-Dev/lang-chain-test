from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import List
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
)


# Clase para definir un CryptoCurrency
class CryptoCurrency(BaseModel):
    name: str = Field(alias="name")
    high: float = Field(alias="high")
    low: float = Field(alias="low")


# Clase para definir la estructura completa de salida (lista de criptomonedas)'
class StructuredOutput(BaseModel):
    date: str = Field(alias="date")
    crypto_currencies: List[CryptoCurrency]


messages = [
    (
        "system",
        "Quiero que el json devuelva 'date' en formato YYYY-MM-DD y 'crypto_currencies' como una lista de criptomonedas, cada una con 'name' string, 'high' float y 'low' float.",
    ),
    (
        "human",
        "Quiero saber el precio más alto y el precio más bajo de ayer de las 10 criptomonedas más populares",
    ),
]

# Configurar el LLM con la salida estructurada
llm = llm.with_structured_output(StructuredOutput, method="json_mode")
message = llm.invoke(messages)

print(message)
