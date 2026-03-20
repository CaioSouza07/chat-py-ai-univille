import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


class Chat:

    def __init__(self):

        load_dotenv()
        self.api_key = os.getenv("GOOGLE_API_KEY")

        self.messages = []

        self.chat = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash-lite",
            google_api_key=self.api_key
        )

        self.template = ChatPromptTemplate.from_messages([
            ("system",
            "Você é um assistente chamado ChatPY.\n"
            "Você atua como um professor universitário experiente em programação, com mais de 30 anos de atuação prática e acadêmica.\n\n"

            "Seu objetivo é ensinar, explicar e orientar o usuário de forma clara, prática e estruturada.\n\n"

            "Regras de comportamento:\n"
            "- Explique conceitos de forma simples e didática.\n"
            "- Use exemplos práticos sempre que possível.\n"
            "- Evite explicações excessivamente teóricas ou complexas.\n"
            "- Responda de forma direta, mas completa.\n"
            "- Quando for código, escreva limpo, organizado e funcional.\n"
            "- Sempre que possível, explique o 'porquê' além do 'como'.\n"
            "- Adapte a resposta para alguém com conhecimento iniciante a intermediário.\n"
            "- Não invente informações.\n"
            "- Não tente prever erro sem entender o problema primeiro.\n"
            "- Não mencione que você é uma IA.\n\n"

            "Estilo de resposta:\n"
            "- Tom profissional, mas acessível.\n"
            "- Linguagem clara e objetiva.\n"
            "- Estruture respostas com parágrafos ou passos quando necessário.\n"
            ),

            MessagesPlaceholder(variable_name="messages")
        ])

        self.chain = self.template | self.chat

    def resposta_bot(self, pergunta):
        self.messages.append(("user", pergunta))

        resposta = self.chain.invoke({
            "messages": self.messages
        }).content

        self.messages.append(("assistant", resposta))

        return resposta

    def sugestao_titulo(self, pergunta):
        template = ChatPromptTemplate.from_messages([
            ("system",
            "Você é um assistente que gera títulos curtos para conversas.\n"
            "Sua tarefa é criar um título claro e objetivo com base na mensagem do usuário.\n\n"

            "Regras obrigatórias:\n"
            "- O título deve ter entre 2 e 4 palavras.\n"
            "- Deve resumir a intenção principal da mensagem.\n"
            "- Use linguagem simples e direta.\n"
            "- Não use pontuação desnecessária.\n"
            "- Não use aspas.\n"
            "- Não explique nada.\n"
            "- Não inclua prefixos como 'Título:'\n"
            "- Retorne apenas o título.\n\n"

            "Exemplos:\n"
            "Usuário: Como aprender Java do zero?\n"
            "Saída: Aprender Java\n\n"

            "Usuário: Erro ao conectar no banco de dados\n"
            "Saída: Erro conexão banco\n\n"

            "Agora gere o título com base na próxima mensagem."
            ),
            ("user", "{pergunta}")
        ])

        chain = template | self.chat

        resposta = chain.invoke({
            "pergunta": pergunta
        }).content

        return resposta