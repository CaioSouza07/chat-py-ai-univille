import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()  # aqui to carregando meu .env onde tem minha chave api bele?

api_key = os.getenv("GOOGLE_API_KEY")

chat = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    google_api_key=api_key
)

def resposta_bot(mensagens):
  mensagens_modelo = [('system', 'Você é um professor universitário da área de programação com mais de 30 anos de experiencia na área, com demasiados projetos realizados')]
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


