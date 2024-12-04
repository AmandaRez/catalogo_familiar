import sqlite3

def conectar_banco():
    conexao = sqlite3.connect("catalogo_familiar.db")
    print("Conexão estabelecida com o banco de dados.")
    return conexao

def criar_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    print("Iniciando a criação das tabelas...")

    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            sexo TEXT,
            idade INTEGER,
            data_nascimento DATE,
            posicao_familiar TEXT NOT NULL,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria_mae_id INTEGER,
            FOREIGN KEY (categoria_mae_id) REFERENCES categorias (id)
        );
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            nome TEXT NOT NULL,
            subcategoria_id INTEGER NOT NULL,
            descricao TEXT,
            material TEXT,
            tamanho TEXT,
            quantidade INTEGER,
            estado TEXT,
            local_armazenamento TEXT,
            estacao TEXT,
            foto BLOB,
            FOREIGN KEY (usuario_id) REFERENCES usuarios (id),
            FOREIGN KEY (subcategoria_id) REFERENCES categorias (id)
        );
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS listas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            nome TEXT NOT NULL,
            descricao TEXT,
            FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
        );
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS listas_produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lista_id INTEGER NOT NULL,
            produto_id INTEGER NOT NULL,
            FOREIGN KEY (lista_id) REFERENCES listas (id),
            FOREIGN KEY (produto_id) REFERENCES produtos (id)
        );
        """)
        
        conexao.commit()
        print("Tabelas criadas ou já existentes.")
    except sqlite3.Error as e:
        print(f"Erro ao criar tabelas: {e}")
    finally:
        conexao.close()   

 
