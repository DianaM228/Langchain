# Code to create API and Use routes to conect with OpenAi and LLAMa APIs (use of Langchain Server)

from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes  # this to create the entire API (routs: interact with OpenAI, interact with llama)
import uvicorn # ASGI web server implementation
import os 
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv("/Users/dianamarin/Documents/Git_Tutorials/Langchain/chatbot/.env")  # Ensure this is before `os.getenv` calls

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="Simple API server"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

model = ChatOpenAI()
llm = Ollama(model="llama2")

prompt1 = ChatPromptTemplate.from_template("Write an essay about {topic} with 80 words")
prompt2 = ChatPromptTemplate.from_template("Write a poem about {topic} on 80 words")

add_routes(
    app,
    prompt1|model,
    path="/essay"
)

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)