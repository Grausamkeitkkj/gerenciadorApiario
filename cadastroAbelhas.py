import tkinter as tk

class CadastroAbelhas:
    def __init__(self, parent):
        self.parent = parent
        self.new_window = tk.Toplevel(parent)
        self.new_window.title("Nova Tela")
        self.new_window.geometry("400x300")
        self.new_window.configure(background="Gray")

        # Criar o campo de escrita (Entry)
        self.nome_abelha_label = tk.Label(self.new_window, text="Nome da Abelha:")
        self.nome_abelha_label.pack()

        self.nome_abelha_entry = tk.Entry(self.new_window)
        self.nome_abelha_entry.pack()

        # Adicione outros widgets e funcionalidades aqui

        # Exemplo de widget:
        label = tk.Label(self.new_window, text="This is the new window!")
        label.pack()
