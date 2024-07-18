import tkinter as tk
from tkinter import ttk
import tabelas
from cadastroAbelhas import cadastroAbelhas
from cadastroCaixas import cadastroCaixas
from tabela_abelha import TreeviewAbelhas

if __name__ == "__main__":
    tabelas.criar_tabelas()

    class Application:
        def __init__(self):
            self.root = tk.Tk()
            self.root.title("Gerenciamento")
            self.root.configure(background="White")
            self.root.geometry("800x500")
            self.create_menu()
            self.root.mainloop()
    
        def create_menu(self):
            menubar = tk.Menu(self.root)
            menu_cadastro = tk.Menu(menubar, tearoff=0)
            menu_relatorios = tk.Menu(menubar, tearoff=0)
            menu_cadastro.add_command(label="Abelhas", command=self.chama_cadastro_abelhas)
            menu_cadastro.add_command(label="Caixas", command=self.chama_cadastro_caixas)
            menu_cadastro.add_command(label="Conectar")
            menubar.add_cascade(label="Cadastro", menu=menu_cadastro)
            menu_relatorios.add_command(label="Relatório de Abelhas", command=self.chama_relatorio_abelhas)
            menubar.add_cascade(label="Relatórios", menu=menu_relatorios)
            self.root.config(menu=menubar)
            
        def chama_cadastro_abelhas(self):
            cadastroAbelhas(self.root)
        
        def chama_cadastro_caixas(self):
            cadastroCaixas(self.root) 
        
        def chama_relatorio_abelhas(self):
            TreeviewAbelhas(self.root)
    
    app = Application()
    