import os
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

#API_KEY = os.getenv("GROQ_API_KEY")

chat = ChatGroq(model='llama-3.3-70b-versatile')

template = ChatPromptTemplate.from_messages(
  [('system', 'Você é um professor renomado em letras com especialização em inglês'),
   ('user', 'Traduza {expressao} para a língua {lingua}')]
)

chain = template | chat

resposta = chain.invoke({'expressao': 'Beleza?', 'lingua': 'inglesa'})
print(resposta.content)