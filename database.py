import sqlite3

def get_connection():
    return sqlite3.connect('chat_database.db')

def criar_tabela_conversas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT
        )
    ''')

    conn.commit()
    conn.close()

def criar_tabela_mensagens():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mensagens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT,
            role TEXT,
            data_hora TEXT,
            id_conversa INTEGER
        )
    ''')

    conn.commit()
    conn.close()

def criar_conversa(titulo):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO conversas (titulo) VALUES (?)"
    cursor.execute(query, (titulo,))

    conn.commit()

    id_conversa = cursor.lastrowid
    conn.close()

    return id_conversa

def inserir_mensagem(mensagem):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO mensagens (message, role, data_hora, id_conversa) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (mensagem['message'], mensagem['role'], mensagem['data_hora'], mensagem['id_conversa']))

    conn.commit()
    conn.close()

def obter_conversas():
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM conversas"
    cursor.execute(query)

    conversas = cursor.fetchall()

    return conversas



def obter_mensagens_conversa(id_conversa):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT role, message 
        FROM mensagens 
        WHERE id_conversa = ?
        ORDER BY data_hora
    """
    cursor.execute(query, (id_conversa,))

    mensagens = cursor.fetchall()

    conn.close()

    return mensagens 
