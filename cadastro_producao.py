import tkinter as tk
from conector_do_DB import get_db_connection
import tkcalendar
from tkinter import messagebox
from tkinter import ttk
import datetime

conn, cursor = get_db_connection()

class CadastroProducao:
    def __init__(self, parent):
        self.parent = parent
        self.new_window = tk.Toplevel(parent)
        self.new_window.title("Cadastro de Produção de Mel")
        self.new_window.geometry("400x300")
        self.new_window.configure(background="White")
        self.opcoes = []
        self.carrega_dados_combobox()

        self.quantidade_mel_label = tk.Label(self.new_window, background="White", text="Quantidade de Mel:")
        self.quantidade_mel_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.quantidade_mel_entry = tk.Entry(self.new_window)
        self.quantidade_mel_entry.grid(row=0, column=1, padx=10, pady=10)

        self.data_producao_label = tk.Label(self.new_window, background="White", text="Data de Produção:")
        self.data_producao_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.data_producao_datepicker = tkcalendar.DateEntry(self.new_window, date_pattern='dd/mm/yyyy', locale='pt_BR')
        self.data_producao_datepicker.grid(row=1, column=1, padx=10, pady=10)

        self.caixa_entry = ttk.Combobox(self.new_window, values=self.opcoes)
        self.caixa_entry.grid(row=2, column=0, padx=10, pady=10)
        self.caixa_entry.set("Selecione a caixa")

        self.salvar_button = tk.Button(self.new_window, text="Salvar", command=lambda: self.salvar_dados())

    def salvar_dados(self):
        quantidade_mel = self.quantidade_mel_entry.get()
        data_producao = self.data_producao_datepicker.get()
        caixa = self.caixa_entry.get()

        try:
            quantidade_mel_float = float(quantidade_mel)
        except ValueError:
            messagebox.showwarning("Aviso", "Quantidade de mel deve ser um número")
            return
        
        if quantidade_mel_float <= 0:
            messagebox.showwarning("Aviso", "Quantidade de Mel deve ser um número maior que 0")
            return
        
        if not quantidade_mel or not data_producao or not caixa:
            messagebox.showwarning("Aviso","Por favor, complete todos os campos antes de salvar")
        else:
            cursor.execute("SELECT id FROM caixas WHERE numero = %s", (caixa,))
            caixa_id = cursor.fetchone()

            if caixa_id:
                cursor.execute("INSERT INTO producao_mel (quantidade, data_producao, caixa_id) VALUES (%s, %s, %s)", (quantidade_mel_float, data_producao, caixa_id))
                conn.commit()
                messagebox.showinfo("Sucesso", "Produção de Mel salva com sucesso")
            else:
                messagebox.showwarning("Aviso", "Caixa não encontrada")

    def carrega_dados_combobox(self):
        cursor.execute("SELECT numero_caixa FROM caixas")
        caixas = cursor.fetchall()
        self.opcoes = [caixa[0] for caixa in caixas]