# ChatPY AI

Aplicação com Python para criar um chatbot conversacional com integração a API do Gemini.

## Sobre o projeto

A aplicação é para fins didáticos, utilizando Python e LangChain para conectar com a API do Gemini 
e simular um chatbot com IA para o usuário, nele é possível:

- Iniciar conversas e persistir os dados;
- Voltar para uma conversa já iniciada e continua-la, sem zerar o contexto;

## Tecnologias utilizadas

- Python
- SQLite
- Streamlit
- LangChain
- API Gemini

## Como rodar

1. Clone o repositório

```cmd
git clone https://github.com/CaioSouza07/chat-py-ai-univille 
```

2. Acesse a pasta do projeto

```cmd
cd chat-py-ai-univille
```

3. Crie um ambiente virtual (venv)

```cmd
python -m venv venv
```

4. Ative a venv

```cmd
venv\Scripts\activate
```

5. Instale as dependências

```cmd
pip install -r requirements.txt
```

6. Configure o arquivo .env com sua chave de API Gemini ([Crie aqui](https://aistudio.google.com/welcome))

- GOOGLE_API_KEY=sua_chave_aqui

7. Execute o projeto

```cmd
streamlit run main.py
```

## Instruções SQL

```sql
-- Criar tabela de conversas
CREATE TABLE IF NOT EXISTS conversas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT
)

-- Criar tabela de mensagens
CREATE TABLE IF NOT EXISTS mensagens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT,
    role TEXT,
    data_hora TEXT,
    id_conversa INTEGER
)
```