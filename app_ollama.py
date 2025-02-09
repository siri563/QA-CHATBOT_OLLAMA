from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os


import os
from dotenv import load_dotenv
load_dotenv()

##Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("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")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGSMITH_PROJECT"] = "Q&A Chatbot With OLLAMA"


##Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
     ("system","you are a helpful assistant. Please response to the user queries"),
     ("user","Questiom:{question}")   
    ]
)


def generate_response(question,engine,temperature,max_tokens):
    llm = Ollama(model=engine)
    output_parser = StrOutputParser()
    chain = prompt|llm|output_parser 
    answer = chain.invoke({'question':question}) 
    return answer



## #Title of the app
st.title("Enhanced Q&A Chatbot With Ollama")


## Select the OpenAI model
llm=st.sidebar.selectbox("Select Open Source model",["mistral"])

## Adjust response parameter
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

## MAin interface for user input
st.write("Goe ahead and ask any question")
user_input=st.text_input("You:")



if user_input :
    response=generate_response(user_input,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please provide the user input")


 
