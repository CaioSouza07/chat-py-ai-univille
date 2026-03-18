import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate


# Atenção Turma: Está é a chave (api_key) do professor e ela será descontínuada após a aula.
# Cada aluno deve considerar em criar uma conta e uma chave. Na aula vou demonstrar quais passo seguir para criar a conta e a chave.


def resposta_bot(mensagens):
  mensagens_modelo = [('system', 'Você é um treinador de futebol da Univille AI ')]
  mensagens_modelo += mensagens
  template = ChatPromptTemplate.from_messages(mensagens_modelo)
  chain = template | chat
  return chain.invoke({}).content

print('Bem-vindo ao Univille AI')

mensagens = []
while True:
  pergunta = input('Usuario: ')
  if pergunta.lower() == 'x':
    break
  mensagens.append(('user', pergunta))
  resposta = resposta_bot(mensagens)
  mensagens.append(('assistant', resposta))
  print(f'Bot: {resposta}')

print('Muito obrigado por usar o Univille AI')
print(mensagens)