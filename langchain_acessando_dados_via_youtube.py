import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import YoutubeLoader
from dotenv import load_dotenv

url='https://www.youtube.com/watch?v=nLopLwffsLI'

load_dotenv()
chat = ChatGroq(model=os.getenv('MODELO'))

loader = YoutubeLoader.from_youtube_url(
  url,
  language=['pt']
)

documento = ''
lista_documentos = loader.load()
for doc in lista_documentos:
  documento += doc.page_content

template = ChatPromptTemplate.from_messages([
  ('system', 'Você é um assistente amigável chamado Asimo e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}'),
  ('user', '{input}')
])

chain = template | chat

pergunta = input('Pergunta: ')
resposta = chain.invoke({ 'documentos_informados': documento, 'input': pergunta })
print(resposta.content)
