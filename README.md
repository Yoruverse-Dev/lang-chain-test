# LLM LangChain

## Setting up environment
LangSmith will be used to trace, debug and monitor our application. And LangChain will be used to handle the LLM models.
#### Installation
```bash
pip install -U langchain langchain-openai langchain langchain_community
# also
pip install wikipedia chromadb pdfplumber 
```
#### Environment Variables
```bash
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY="<your-api-key>"
LANGCHAIN_PROJECT="Yoruverse"
```

#### Running the application
We will need access to the environment variables in the application. We can use the `python-dotenv` package to load the environment variables from a `.env` file.
```bash
pip install python-dotenv
```

```python
from dotenv import load_dotenv
load_dotenv()
```