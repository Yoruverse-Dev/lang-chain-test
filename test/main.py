from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import List
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
)

messages = [
    (
        "system",
        "Quiero que el json devuelva una lista de jugadores, cada uno con 'name' string, 'age' int y 'height' int.",
    ),
    (
        "human",
        "Quiero saber la altura y la edad de los 3 jugadores de baloncesto más famosos de la historia.",
    ),
]


# Clase para definir un solo jugador
class Jugador(BaseModel):
    nombre: str = Field(alias="name")
    edad: int = Field(alias="age")
    estatura: int = Field(alias="height")


# Clase para definir la estructura completa de salida (lista de jugadores)
class StructuredOutput(BaseModel):
    jugadores: List[Jugador] = Field(alias="players")


# Configurar el LLM con la salida estructurada
llm = llm.with_structured_output(StructuredOutput, method="json_mode")
message = llm.invoke(messages)

print(message)
