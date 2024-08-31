import tkinter as tk
from tkinter import ttk
import tkcalendar
import datetime
from tkinter import messagebox
from conector_do_DB import get_db_connection

conn, cursor = get_db_connection()

class CadastroProducao:
    def __init__(self, parent):
        self.parent = parent
        self.new_window = tk.Toplevel(parent)
        self.new_window.title("Cadastro de Caixas")
        self.new_window.geometry("400x300")
        self.new_window.configure(background="White")
        self.opcoes = []
        self.carrega_dados_combobox()

        self.producao_label = tk.Label(self.new_window, background="White", text="Quantidade de Produção")
        self.producao_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.producao_entry = tk.Entry(self.new_window)
        self.producao_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.numero_caixa_label = tk.Label(self.new_window, background="White", text="Número Caixa:")
        self.numero_caixa_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.numero_caixa_entry = ttk.Combobox(self.new_window, values=self.opcoes)
        self.numero_caixa_entry.grid(row=1, column=1, padx=10, pady=10)
        self.numero_caixa_entry.set("Selecione a caixa")

        self.data_producao_label = tk.Label(self.new_window, background="White", text="Data de produção:")
        self.data_producao_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.data_producao_datepicker = tkcalendar.DateEntry(self.new_window, date_pattern='dd/mm/yyyy', locale='pt_BR')
        self.data_producao_datepicker.grid(row=3, column=1, padx=10, pady=10)

        self.salvar_button = tk.Button(self.new_window, text="Salvar", command=lambda:[self.salva_dados_caixa()])
        self.salvar_button.grid(row=4, column=0, columnspan=2, padx=36, pady=10)
        self.salvar_button.place(relx=0.5, rely=0.9,relwidth=0.50, relheight=0.15, anchor='center')

    def salva_dados_caixa(self):
        producao = self.producao_entry.get()
        numero_caixa = int(self.numero_caixa_entry.get())
        data_producao = self.data_producao_datepicker.get()
        data_producao_sql = datetime.datetime.strptime(data_producao, '%d/%m/%Y').strftime('%Y-%m-%d')
    
        if not producao or not numero_caixa or not data_producao:
            messagebox.showwarning("Aviso","Por favor, complete todos os campos antes de salvar")
        else:
            cursor.execute("SELECT id FROM caixas WHERE numero_caixa = %s", (numero_caixa,))
            caixa_id = cursor.fetchone()
    
            if caixa_id:
                cursor.execute("INSERT INTO producao_mel (data, quantidade, caixa_id) VALUES (%s, %s, %s)",
                    (data_producao_sql, producao, caixa_id[0]))
                conn.commit()
                messagebox.showinfo("Aviso","Dados salvos com sucesso")
                self.producao_entry.delete(0, tk.END)
                self.numero_caixa_entry.delete(0, tk.END)
                self.data_producao_datepicker.delete(0, tk.END)
            else:
                messagebox.showwarning("Aviso", "Espécie não encontrada.")

    def carrega_dados_combobox(self):
        cursor.execute("SELECT numero_caixa FROM caixas")
        rows = cursor.fetchall()
        for row in rows:
            self.opcoes.append(row[0])