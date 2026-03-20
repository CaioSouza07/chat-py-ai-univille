import streamlit as st
from database import *
from chat import Chat
from datetime import datetime

if "id_conversa" not in st.session_state:
    st.session_state.id_conversa = None

if "chat" not in st.session_state:
    st.session_state.chat = Chat()



st.set_page_config(
    page_title="ChatPY",
    layout="centered"
)

st.title("ChatPY")

with st.sidebar:
    st.title("Menu")

    if st.button("➕ Nova conversa", type="primary"):
        st.session_state.id_conversa = None
        st.session_state.chat.messages = []
        st.rerun()

    conversas = obter_conversas()

    # st.divider()
    st.subheader("Seus chats")

    for conversa in reversed(conversas):
        if st.button(conversa[1]):
            st.session_state.id_conversa = conversa[0]
            mensagens = obter_mensagens_conversa(conversa[0])

            st.session_state.chat.messages = [
                msg for msg in mensagens
            ]
            st.rerun()

st.markdown("---")

for role, msg in st.session_state.chat.messages:
    if role == "user":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)

prompt = st.chat_input("Digite sua pergunta...")

if prompt:
    if st.session_state.id_conversa is None:
        titulo = st.session_state.chat.sugestao_titulo(prompt)
        st.session_state.id_conversa = criar_conversa(titulo)

    resposta = st.session_state.chat.resposta_bot(prompt)
    agora = datetime.now()
    formatado = agora.strftime("%d/%m/%Y %H:%M:%S")

    resposta_user = {
        "message": prompt,
        "role": "user",
        "data_hora": formatado,
        "id_conversa": st.session_state.id_conversa
    }

    resposta_chat = {
        "message": resposta,
        "role": "assistant",
        "data_hora": formatado,
        "id_conversa": st.session_state.id_conversa
    }

    inserir_mensagem(resposta_user)
    inserir_mensagem(resposta_chat)

    # st.session_state.chat.messages.append(("user", prompt))
    # st.session_state.chat.messages.append(("assistant", resposta))

    prompt = False

    st.rerun()