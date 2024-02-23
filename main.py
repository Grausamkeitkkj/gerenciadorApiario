import tkinter as tk
from cadastroAbelhas import CadastroAbelhas

class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gerenciamento")
        self.root.configure(background="Gray")
        self.root.geometry("800x500")
        self.create_menu()
        self.root.mainloop()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Abelhas", command=self.chama_cadastro_abelhas)
        menubar.add_cascade(label="Cadastro", menu=file_menu)
        self.root.config(menu=menubar)

    def chama_cadastro_abelhas(self):
        cadastro_window = CadastroAbelhas(self.root) 

        cadastro_window.mainloop()

app = Application()