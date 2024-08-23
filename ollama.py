from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import os
import streamlit as st
from dotenv import load_dotenv



load_dotenv()
#Creating the Lang Smith logger
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] ="ollama-llama-v2"

#Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant.Please response to the user query"),
     ("user","Question:{question}")
     ]
)

#streamlit App
st.title("Langchain chatbot using Llama2")
input_text = st.text_input("Write your Query")

#Model Defining LLama2
llm = Ollama(model = "llama2")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))

