import sqlite3

def conectar_banco():
    conexao = sqlite3.connect(r"C:\Users\amand\Documentos\Projetos Particulares\Catálogo familiar\catalogo_familiar\catalogo_familiar.db")
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


def adicionar_usuario(nome, sexo, idade, data_nascimento, posicao_familiar):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        cursor.execute("""
        INSERT INTO usuarios (nome, sexo, idade, data_nascimento, posicao_familiar)
        VALUES (?, ?, ?, ?, ?);
        """, (nome, sexo, idade, data_nascimento, posicao_familiar))
        conexao.commit()
        print(f"Usuário {nome} adicionado com sucesso.")
    except sqlite3.IntegrityError as e:
        print(f"Erro ao adicionar usuário: {e}")
    finally:
        conexao.close()

def listar_usuarios():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM usuarios;")
    usuarios = cursor.fetchall()
    
    conexao.close()
    return usuarios

def adicionar_categoria(nome, categoria_mae_id=None):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        cursor.execute("""
        INSERT INTO categorias (nome, categoria_mae_id)
        VALUES (?, ?);
        """, (nome, categoria_mae_id))
        conexao.commit()
        print(f"Categoria '{nome}' adicionada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao adicionar categoria: {e}")
    finally:
        conexao.close()

def adicionar_produto(usuario_id, subcategoria_id, nome, descricao, material, tamanho, quantidade, estado, local_armazenamento, estacao, foto=None):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        cursor.execute("""
        INSERT INTO produtos (usuario_id, subcategoria_id, nome, descricao, material, tamanho, quantidade, estado, local_armazenamento, estacao, foto)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (usuario_id, subcategoria_id, nome, descricao, material, tamanho, quantidade, estado, local_armazenamento, estacao, foto))
        conexao.commit()
        print(f"Produto '{nome}' adicionado com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao adicionar produto: {e}")
    finally:
        conexao.close()

def atualizar_usuario(usuario_id, nome=None, sexo=None, idade=None, data_nascimento=None, posicao_familiar=None):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        query = "UPDATE usuarios SET "
        valores = []
        
        if nome:
            query += "nome = ?, "
            valores.append(nome)
        if sexo:
            query += "sexo = ?, "
            valores.append(sexo)
        if idade:
            query += "idade = ?, "
            valores.append(idade)
        if data_nascimento:
            query += "data_nascimento = ?, "
            valores.append(data_nascimento)
        if posicao_familiar:
            query += "posicao_familiar = ?, "
            valores.append(posicao_familiar)
        
        query = query.rstrip(", ")
        query += " WHERE id = ?"
        valores.append(usuario_id)
        
        cursor.execute(query, valores)
        conexao.commit()
        print(f"Usuário ID {usuario_id} atualizado com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao atualizar usuário: {e}")
    finally:
        conexao.close()

def excluir_usuario(usuario_id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (usuario_id,))
        conexao.commit()
        print(f"Usuário ID {usuario_id} excluído com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao excluir usuário: {e}")
    finally:
        conexao.close()

def atualizar_categoria(categoria_id, nome=None, categoria_mae_id=None):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        query = "UPDATE categorias SET "
        valores = []
        
        if nome:
            query += "nome = ?, "
            valores.append(nome)
        if categoria_mae_id is not None:
            query += "categoria_mae_id = ?, "
            valores.append(categoria_mae_id)
        
        query = query.rstrip(", ")
        query += " WHERE id = ?"
        valores.append(categoria_id)
        
        cursor.execute(query, valores)
        conexao.commit()
        print(f"Categoria ID {categoria_id} atualizada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao atualizar categoria: {e}")
    finally:
        conexao.close()

def excluir_categoria(categoria_id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        cursor.execute("DELETE FROM categorias WHERE id = ?", (categoria_id,))
        conexao.commit()
        print(f"Categoria ID {categoria_id} excluída com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao excluir categoria: {e}")
    finally:
        conexao.close()

def atualizar_produto(produto_id, **kwargs):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        query = "UPDATE produtos SET "
        valores = []
        
        for coluna, valor in kwargs.items():
            query += f"{coluna} = ?, "
            valores.append(valor)
        
        query = query.rstrip(", ")
        query += " WHERE id = ?"
        valores.append(produto_id)
        
        cursor.execute(query, valores)
        conexao.commit()
        print(f"Produto ID {produto_id} atualizado com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao atualizar produto: {e}")
    finally:
        conexao.close()

def excluir_produto(produto_id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        cursor.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
        conexao.commit()
        print(f"Produto ID {produto_id} excluído com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao excluir produto: {e}")
    finally:
        conexao.close()

if __name__ == "__main__":
    # Criar as tabelas e adicionar dados de exemplo
    criar_tabelas()
    
