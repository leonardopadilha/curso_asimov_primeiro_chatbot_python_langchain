import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader

load_dotenv()

chat = ChatGroq(model='llama-3.3-70b-versatile')

loader = WebBaseLoader('https://asimov.academy/')
lista_documents = loader.load()

# documento = lista_documents[0].page_content

documento = ''
for doc in lista_documents:
  documento += doc.page_content
# print(documento)

template = ChatPromptTemplate.from_messages([
  ('system', 'Você é um assistente amigável chamado Asimo e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}'),
  ('user', '{input}')
])

chain = template | chat

pergunta = input('Pergunta: ')
resposta = chain.invoke({'documentos_informados': documento, 'input': pergunta})
print(resposta.content)
