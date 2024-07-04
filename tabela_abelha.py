import tkinter as tk
from tkinter import ttk
import psycopg2
import conector

conn = conector.conn
cursor = conn.cursor()

class TreeviewAbelhas:
    def __init__(self, master):
        self.master = master
        self.lista_abelhas = ttk.Treeview(self.master, height=3, column=("col1", "col2", "col3", "col4", "col5"))
        self.lista_abelhas.heading("#0", text="")
        self.lista_abelhas.heading("#1", text="Espécie")
        self.lista_abelhas.heading("#2", text="Nome Científico")
        self.lista_abelhas.heading("#3", text="Localização")
        self.lista_abelhas.heading("#4", text="Data de Aquisição")
        self.lista_abelhas.heading("#5", text="Caixa")

        self.lista_abelhas.column("#0", width=1)
        self.lista_abelhas.column("#1", width=100)
        self.lista_abelhas.column("#2", width=120)
        self.lista_abelhas.column("#3", width=70)
        self.lista_abelhas.column("#4", width=70)
        self.lista_abelhas.column("#5", width=40)

        self.lista_abelhas.place(x=40, y=10, width=700, height=300)
        self.scroolbar = tk.Scrollbar(self.master, orient='vertical', command=self.lista_abelhas.yview)
        self.lista_abelhas.configure(yscrollcommand=self.scroolbar.set)
        self.scroolbar.place(x=740, y=10, height=300)
        self.carrega_dados_abelha()

    def carrega_dados_abelha(self):
        cursor.execute("SELECT especie, nome_cientifico, localizacao, TO_CHAR(data_aquisicao, 'DD/MM/YYYY') AS data_formatada, caixa FROM abelhas")
        rows = cursor.fetchall()

        for i in self.lista_abelhas.get_children():
            self.lista_abelhas.delete(i)

        for row in rows:
            self.lista_abelhas.insert("", "end", values=row)
