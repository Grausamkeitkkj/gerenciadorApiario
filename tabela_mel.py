import tkinter as tk
from tkinter import ttk, messagebox
from conector_do_DB import get_db_connection

conn, cursor = get_db_connection()

class TreeviewMel:
    def __init__(self, parent):
        self.parent = parent
        self.new_window = tk.Toplevel(parent)
        self.new_window.title("Cadastro Produção de Mel")
        self.new_window.geometry("825x450")
        self.new_window.configure(background="White")

        self.master = parent
        self.lista_mel = ttk.Treeview(self.new_window, height=3, column=("col1", "col2", "col3", "col4", "col5", "col6"))
        self.lista_mel.heading("#0", text="")
        self.lista_mel.heading("#1", text="ID")
        self.lista_mel.heading("#2", text="Número da Caixa")
        self.lista_mel.heading("#3", text="Mês 1")
        self.lista_mel.heading("#4", text="Mês 2")
        self.lista_mel.heading("#5", text="Mês 3")
        self.lista_mel.heading("#6", text="Mês 4")
        self.lista_mel.heading("#7", text="Mês 5")
        self.lista_mel.heading("#8", text="Mês 6")
        self.lista_mel.heading("#9", text="Mês 7")
        self.lista_mel.heading("#10", text="Mês 8")
        self.lista_mel.heading("#11", text="Mês 9")
        self.lista_mel.heading("#12", text="Mês 10")
        self.lista_mel.heading("#12", text="Mês 11")
        self.lista_mel.heading("#12", text="Mês 12")

        self.lista_mel.column("#0", width=1)
        self.lista_mel.column("#1", width=8)
        self.lista_mel.column("#2", width=100)
        self.lista_mel.column("#3", width=120)
        self.lista_mel.column("#4", width=70)
        self.lista_mel.column("#5", width=70)
        self.lista_mel.column("#6", width=40)
        self.lista_mel.column("#7", width=40)
        self.lista_mel.column("#8", width=40)
        self.lista_mel.column("#9", width=40)
        self.lista_mel.column("#10", width=40)
        self.lista_mel.column("#11", width=40)
        self.lista_mel.column("#12", width=40)

        self.lista_mel.place(x=40, y=40, width=700, height=300)
        
        self.scroolbar = tk.Scrollbar(self.new_window, orient='vertical', command=self.lista_mel.yview)
        self.scroolbar.place(x=740, y=40, height=300)
        self.lista_mel.configure(yscrollcommand=self.scroolbar.set)

        self.label_informativo = tk.Label(self.new_window, text="", font=(14), bg="white")
        self.label_informativo.grid(row=0, column=0, padx=35, pady=10, sticky='w')

        self.apagar_button = tk.Button(self.new_window, text="Cadastrar Produção", command=self.chama_cadastro_mel)
        self.apagar_button.place(x=40, y=350, width=100, height=30)

        self.carrega_dados_mel()

    def carrega_dados_mel(self):
        cursor.execute("SELECT * FROM mel WHERE data_recolhimento >= DATEADD(MONTH, -12, GETDATE()) ORDER BY data_recolhimento DESC LIMIT 12; ")
        rows = cursor.fetchall()

        for i in self.lista_mel.get_children():
            self.lista_mel.delete(i)

        for row in rows:
            self.lista_mel.insert("", "end", values=row)