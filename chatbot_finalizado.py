import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.document_loaders import PyPDFLoader

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('GROQ_API_KEY')
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.3-70b-versatile')

documento = ''
def carrega_site():
  url_site = input('Digite a url do site: ')

  loader = WebBaseLoader(url_site)
  lista_documentos = loader.load()
  
  documento = ''
  for doc in lista_documentos:
    documento += doc.page_content
  return documento

def carrega_pdf():
  loader = PyPDFLoader('dados/salmos.pdf')
  lista_documentos = loader.load()
  documento = ''
  for doc in lista_documentos:
    documento += doc.page_content
  return documento

def carrega_youtube():
  url_youtube = input('Digite a url do vídeo: ')
  loader = YoutubeLoader.from_youtube_url(
    url_youtube,
    language=['pt']
  )
  lista_documentos = loader.load()
  documento = ''
  for doc in lista_documentos:
    documento += doc.page_content
  return documento


def resposta_bot(mensagens, documento):
  mensagem_sistema = '''Você é um assistente amigável chamado Asimo.
  Você utiliza as seguintes informações para formular suas respostas: {informacoes}
  '''

  mensagens_modelo = [('system', mensagem_sistema)]
  mensagens_modelo += mensagens

  template = ChatPromptTemplate.from_messages(mensagens_modelo)
  chain = template | chat
  return chain.invoke({'informacoes': documento}).content

print('Bem-vindo ao AsimoBot')

texto_selecao = '''Digite a opção desejada:
1. Conversar com um site;
2. Conversar com um pdf;
3. Conversar com um vídeo de youtube
'''

while True:
  selecao = input(texto_selecao)
  if selecao == '1':
    documento = carrega_site()
    break
  if selecao == '2':
    documento = carrega_pdf()
    break
  if selecao == '3':
    documento = carrega_youtube()
    break
  print('Digite um número válido')

mensagens = []
while True:
  pergunta = input('Usuário: ')
  if pergunta.lower() == 'x':
    break
  mensagens.append(('user', pergunta ))
  resposta = resposta_bot(mensagens, documento)
  mensagens.append(('assistant', resposta ))
  print(f'Bot: {resposta}')

print('Muito obrigado por usar o AsimoBot')