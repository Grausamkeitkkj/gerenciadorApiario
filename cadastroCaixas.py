import tkinter as tk
import conector

class cadastroCaixas:
    def __init__(self, parent):
        self.parent = parent
        self.new_window = tk.Toplevel(parent)
        self.new_window.title("Cadastro de Caixas")
        self.new_window.geometry("400x300")
        self.new_window.configure(background="White")