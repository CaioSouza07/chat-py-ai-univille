import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

class Chat:

    def __init__(self):

        load_dotenv()  # aqui to carregando meu .env onde tem minha chave api bele?
        self.api_key = os.getenv("GOOGLE_API_KEY")

        self.messages = []

        self.chat = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash-lite",
            google_api_key=self.api_key
        )

    def resposta_bot(self, pergunta):
        self.messages.append(('user', pergunta))
        mensagens_modelo = [('system', 'Você é um professor universitário da área de programação com mais de 30 anos de experiencia na área, com demasiados projetos realizados')]
        mensagens_modelo += self.messages
        template = ChatPromptTemplate.from_messages(mensagens_modelo)
        chain = template | self.chat
        resposta = chain.invoke({}).content
        self.messages.append(('assistant', resposta))
        return resposta
    

