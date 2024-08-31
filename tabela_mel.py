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
        self.lista_mel.heading("#1", text="")
        self.lista_mel.heading("#2", text="")
        self.lista_mel.heading("#3", text="")
        self.lista_mel.heading("#4", text="")
        self.lista_mel.heading("#5", text="")

        self.lista_mel.column("#0", width=1)
        self.lista_mel.column("#1", width=8)
        self.lista_mel.column("#2", width=100)
        self.lista_mel.column("#3", width=120)
        self.lista_mel.column("#4", width=70)
        self.lista_mel.column("#5", width=70)
        self.lista_mel.column("#6", width=40)

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
        cursor.execute("")
        rows = cursor.fetchall()

        for i in self.lista_mel.get_children():
            self.lista_mel.delete(i)

        for row in rows:
            self.lista_mel.insert("", "end", values=row)

    def apagar_abelha(self):
        if not self.lista_mel.selection():
            messagebox.showwarning("Aviso", "Por favor, selecione um item para apagar")
        elif messagebox.askokcancel("Confirmação", "Deseja realmente apagar o item selecionado?"):
            for each_item in self.lista_mel.selection():
                id = self.lista_mel.item(each_item, 'values')[0]
                cursor.execute()
                cursor.execute()
            conn.commit()
            self.carrega_dados_abelha()

    def chama_cadastro_mel(self):
        pass