import sqlite3

def criar_banco():
    conn = sqlite3.connect("catalogo.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS perfis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def salvar_perfil(nome, idade):
    conn = sqlite3.connect("catalogo.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO perfis (nome, idade) VALUES (?, ?)", (nome, idade))
    conn.commit()
    conn.close()

def carregar_perfis():
    conn = sqlite3.connect("catalogo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nome, idade FROM perfis")
    perfis = cursor.fetchall()
    conn.close()
    return perfis
