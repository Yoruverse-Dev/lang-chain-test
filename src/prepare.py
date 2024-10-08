# Load env variables
from dotenv import load_dotenv

load_dotenv()

# Load documents
from langchain_community.document_loaders import DirectoryLoader, PDFPlumberLoader

DATA_PATH = "./src/static"


def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.pdf", loader_cls=PDFPlumberLoader)
    return loader.load()


# Split documents into chunks
from langchain.text_splitter import RecursiveCharacterTextSplitter


def split_text(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000, chunk_overlap=500, length_function=len, add_start_index=True
    )

    chunks = text_splitter.split_documents(documents)

    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")
    return chunks


chunks = split_text(load_documents())

# Create chroma db
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
import os
import shutil


def save_to_db(chunks):

    CHROMA_PATH = "db"

    if os.path.exists(CHROMA_PATH):
        print("Deleting existing db...")
        shutil.rmtree(CHROMA_PATH)

    db = Chroma.from_documents(
        chunks, OpenAIEmbeddings(), persist_directory=CHROMA_PATH
    )

    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")
    return db


db = save_to_db(chunks)
