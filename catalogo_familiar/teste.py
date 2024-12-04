"""def atualizar_usuario(usuario_id, nome=None, sexo=None, idade=None, data_nascimento=None, posicao_familiar=None):
    
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    campos = []
    valores = []
    
    if nome:
        campos.append("nome = ?")
        valores.append(nome)
    if sexo:
        campos.append("sexo = ?")
        valores.append(sexo)
    if idade:
        campos.append("idade = ?")
        valores.append(idade)
    if data_nascimento:
        campos.append("data_nascimento = ?")
        valores.append(data_nascimento)
    if posicao_familiar:
        campos.append("posicao_familiar = ?")
        valores.append(posicao_familiar)
    
    valores.append(usuario_id)
    
    sql = f"UPDATE usuarios SET {', '.join(campos)} WHERE id = ?;"
    cursor.execute(sql, valores)
    
    conexao.commit()
    print(f"Usuário {usuario_id} atualizado com sucesso.")
    conexao.close()

def excluir_usuario(usuario_id):
    
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute("DELETE FROM usuarios WHERE id = ?;", (usuario_id,))
    
    conexao.commit()
    print(f"Usuário {usuario_id} excluído com sucesso.")
    conexao.close()

def excluir_produto(produto_id):
    
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute("DELETE FROM produtos WHERE id = ?;", (produto_id,))
    
    conexao.commit()
    print(f"Produto {produto_id} excluído com sucesso.")
    conexao.close()



if __name__ == "__main__":
    atualizar_usuario(1, nome="Amanda Souza", idade=31)
if __name__ == "__main__":
    excluir_produto(1)

    Próximos Passos
Criar uma função para popular automaticamente as categorias/subcategorias.
Validar as entradas de dados.
Integrar os métodos ao módulo gráfico.







#testes
if __name__ == "__main__":
    # Criar as tabelas e adicionar dados de exemplo
    criar_tabelas()
    
    adicionar_usuario("Amanda", "Feminino", 38, "1986-12-06", "Mãe")
    usuarios = listar_usuarios()
    for usuario in usuarios:
        print(usuario)
    
    adicionar_categoria("Calçados", None)  # Nenhuma categoria mãe
    
    adicionar_produto(
        usuario_id=1,
        subcategoria_id=1,
        nome="Tênis Esportivo",
        descricao="Tênis leve e confortável",
        material="Couro sintético",
        tamanho="42",
        quantidade=2,
        estado="Novo",
        local_armazenamento="Armário Superior",
        estacao="Todas",
        foto=None  # Aqui você pode inserir bytes de uma imagem no futuro
    )"""