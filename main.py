import tkinter as tk
from tkinter import ttk
import tabelas
from cadastroAbelhas import cadastroAbelhas
from cadastroCaixas import cadastroCaixas
from tabela_abelha import TreeviewAbelhas
from cadastro_producao import CadastroProducao
from tabela_mel import TreeviewMel

if __name__ == "__main__":
    tabelas.criar_tabelas()

    class Application:
        def __init__(self):
            self.dicionario = {}
            self.root = tk.Tk()
            self.root.iconbitmap(r'.\bee.ico')
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
            menu_cadastro.add_command(label="Produção de Mel", command=self.chama_cadastro_mel)
            menu_relatorios.add_command(label="Relatório de Abelhas", command=self.chama_relatorio_abelhas)
            menu_relatorios.add_command(label="Relatório Produção de Mel", command=self.chama_relatorio_mel)
            menubar.add_cascade(label="Cadastro", menu=menu_cadastro)
            menubar.add_cascade(label="Relatórios", menu=menu_relatorios)
            self.root.config(menu=menubar)
            
        def chama_cadastro_abelhas(self):
            cadastroAbelhas(self.root, self.tentar_chamar_funcao)
        
        def chama_cadastro_caixas(self):
            cadastroCaixas(self.root) 
        
        def chama_relatorio_abelhas(self):
            TreeviewAbelhas(self.root, self.dicionario, self.tentar_chamar_funcao)

        def chama_relatorio_mel(self):
           TreeviewMel(self.root)
    
        def tentar_chamar_funcao(self):
            if self.dicionario.get("carregar_abelhas"):
                self.dicionario["carregar_abelhas"]()


    app = Application()
    