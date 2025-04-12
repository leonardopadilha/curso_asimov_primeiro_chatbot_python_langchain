import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

chat = ChatGroq(model='llama-3.3-70b-versatile')

resposta = chat.invoke('Olá, modelo! Quem é você?')
print(resposta.content)
