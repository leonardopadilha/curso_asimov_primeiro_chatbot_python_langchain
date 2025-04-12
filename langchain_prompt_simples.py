from langchain.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages(
  [('user', 'Traduza {expressao} para a língua {lingua}')]
)

resposta = template.invoke({'expressao': 'Beleza?', 'lingua': 'inglesa'})
print(resposta.messages[0].content)