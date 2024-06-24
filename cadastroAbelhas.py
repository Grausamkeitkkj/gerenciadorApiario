import tkinter as tk
import conector

class cadastroAbelhas:
    def __init__(self, parent):
        self.parent = parent
        self.new_window = tk.Toplevel(parent)
        self.new_window.title("Cadastro de Abelhas")
        self.new_window.geometry("400x300")
        self.new_window.configure(background="White")

        self.especie_abelha_label = tk.Label(self.new_window, background="White", text="Espécie:")
        self.especie_abelha_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.nome_abelha_entry = tk.Entry(self.new_window)
        self.nome_abelha_entry.grid(row=0, column=1, padx=10, pady=10)

        self.especie_cientifica_abelha_label = tk.Label(self.new_window, background="White", text="Nome científico:")
        self.especie_cientifica_abelha_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.especie_abelha_entry = tk.Entry(self.new_window)
        self.especie_abelha_entry.grid(row=1, column=1, padx=10, pady=10)

        self.localizacao_label = tk.Label(self.new_window, background="White", text="Localização:")
        self.localizacao_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.localizacao_entry = tk.Entry(self.new_window)
        self.localizacao_entry.grid(row=2, column=1, padx=10, pady=10)