
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser # tools to use the model output (e.g., display, capital letter)
import streamlit as st # turns data scripts into shareable web apps
import os
from dotenv import load_dotenv # reads key-value pairs from a .env file and can set them as environment variables

load_dotenv("/Users/dianamarin/Documents/Git_Tutorials/Langchain/chatbot/.env")  # Ensure this is before `os.getenv` calls


os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

print("LANGCHAIN_API_KEY:", os.getenv("LANGCHAIN_API_KEY"))
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))


## promt template definition

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to user queries"),
        ("user","Question:{question}")
    ]

)

# steamlit framework
st.title("Langchain Demo with OpenAI API")
input_text=st.text_input("Search the topic u want")

# Call the LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
# cahin -> combine everithing we defined 
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))


