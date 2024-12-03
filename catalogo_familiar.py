import tkinter as tk
from banco_dados import criar_banco, salvar_perfil, carregar_perfis

# Função para adicionar perfil
def adicionar_perfil():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    
    if nome and idade:
        salvar_perfil(nome, idade)
        lista_perfis.insert(tk.END, f"{nome} - {idade} anos")
        entrada_nome.delete(0, tk.END)
        entrada_idade.delete(0, tk.END)
    else:
        print("Por favor, preencha todos os campos!")

# Interface Gráfica
criar_banco()  # Garante que o banco existe ao iniciar
janela = tk.Tk()
janela.title("Catálogo Familiar")
janela.geometry("400x400")

tk.Label(janela, text="Nome:").pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()

tk.Label(janela, text="Idade:").pack()
entrada_idade = tk.Entry(janela)
entrada_idade.pack()

botao_adicionar = tk.Button(janela, text="Adicionar Perfil", command=adicionar_perfil)
botao_adicionar.pack(pady=10)

lista_perfis = tk.Listbox(janela)
lista_perfis.pack(pady=10, fill=tk.BOTH, expand=True)

# Carregar perfis do banco
for perfil in carregar_perfis():
    lista_perfis.insert(tk.END, f"{perfil[0]} - {perfil[1]} anos")

janela.mainloop()
