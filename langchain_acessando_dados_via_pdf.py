import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv

caminho_arquivo_pdf = 'dados/salmos.pdf'

load_dotenv()

chat = ChatGroq(model=os.getenv('MODELO'))

loader = PyPDFLoader(caminho_arquivo_pdf)
lista_documentos = loader.load()

documento = ''
for doc in lista_documentos:
  documento += doc.page_content

#try:
#  print(documento.encode('utf-8').decode('utf-8'))
#except UnicodeEncodeError as e:
#  print(f"Erro ao imprimir documento: {e}")

template = ChatPromptTemplate.from_messages([
  ('system', 'Você é um assistente amigável chamado Asimo e tem acesso as seguintes informações para dar as suas respostas: {arquivo}'),
  ('user', '{input}')
])

chain = template | chat
pergunta = input('Pergunta: ')
resposta = chain.invoke({'arquivo': documento, 'input': pergunta })
#print(resposta.content)

