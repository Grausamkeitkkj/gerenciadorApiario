import tkinter as tk
import conector
import tkcalendar
from tkinter import messagebox
from tabela_abelha import TreeviewAbelhas

conn = conector.conn
cursor = conn.cursor()

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

        self.data_aquisicao_label = tk.Label(self.new_window, background="White", text="Data de aquisição:")
        self.data_aquisicao_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.data_aquisicao_datepicker = tkcalendar.DateEntry(self.new_window, date_pattern='dd/mm/yyyy', locale='pt_BR')
        self.data_aquisicao_datepicker.grid(row=3, column=1, padx=10, pady=10)

        self.caixa_label = tk.Label(self.new_window, background="White", text="Caixa:")
        self.caixa_label.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        self.caixa_entry = tk.Entry(self.new_window)
        self.caixa_entry.grid(row=4, column=1, padx=10, pady=10)

        self.salvar_button = tk.Button(self.new_window, text="Salvar", command=lambda:[self.salvar_dados(), TreeviewAbelhas(self.parent).carrega_dados_abelha()])
        self.salvar_button.grid(row=4, column=0, columnspan=2, padx=36, pady=10)
        self.salvar_button.place(relx=0.5, rely=0.9,relwidth=0.50, relheight=0.15, anchor='center')

    def salvar_dados(self):
        especie = self.nome_abelha_entry.get()
        nome_cientifico = self.especie_abelha_entry.get()
        localizacao = self.localizacao_entry.get()
        data_aquisicao = self.data_aquisicao_datepicker.get()
        caixa = self.caixa_entry.get()
    
        if not especie or not nome_cientifico or not localizacao or not data_aquisicao:
            messagebox.showwarning("Aviso","Por favor, complete todos os campos antes de salvar")
        else:
            cursor.execute(("INSERT INTO abelhas (especie, nome_cientifico, localizacao, data_aquisicao, caixa) VALUES (%s, %s, %s, %s, %s)"),
                (especie, nome_cientifico, localizacao, data_aquisicao, caixa)
            )
            messagebox.showinfo("Aviso","Dados salvos com sucesso")
            conn.commit()
            self.nome_abelha_entry.delete(0, tk.END)
            self.especie_abelha_entry.delete(0, tk.END)
            self.localizacao_entry.delete(0, tk.END)
            self.caixa_entry.delete(0, tk.END)