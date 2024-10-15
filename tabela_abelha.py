import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
from conector_do_DB import get_db_connection
from cadastroAbelhas import cadastroAbelhas
import psycopg2

conn, cursor = get_db_connection()

class TreeviewAbelhas:
    def __init__(self, parent):
        self.parent = parent
        self.new_window = tk.Toplevel(parent)
        self.new_window.title("Cadastro de Abelhas")
        self.new_window.geometry("825x450")
        self.new_window.configure(background="White")

        self.master = parent
        self.lista_abelhas = ttk.Treeview(self.new_window, height=3, column=("col1", "col2", "col3", "col4", "col5", "col6"))
        self.lista_abelhas.heading("#0", text="")
        self.lista_abelhas.heading("#1", text="ID")
        self.lista_abelhas.heading("#2", text="Espécie")
        self.lista_abelhas.heading("#3", text="Nome Científico")
        self.lista_abelhas.heading("#4", text="Localização")
        self.lista_abelhas.heading("#5", text="Data de Aquisição")
        self.lista_abelhas.heading("#6", text="Caixa")

        self.lista_abelhas.column("#0", width=1)
        self.lista_abelhas.column("#1", width=8)
        self.lista_abelhas.column("#2", width=100)
        self.lista_abelhas.column("#3", width=120)
        self.lista_abelhas.column("#4", width=70)
        self.lista_abelhas.column("#5", width=70)
        self.lista_abelhas.column("#6", width=40)

        self.lista_abelhas.place(x=40, y=40, width=700, height=300)
        
        self.scroolbar = tk.Scrollbar(self.new_window, orient='vertical', command=self.lista_abelhas.yview)
        self.scroolbar.place(x=740, y=40, height=300)
        self.lista_abelhas.configure(yscrollcommand=self.scroolbar.set)

        self.label_informativo = tk.Label(self.new_window, text="Listagem Abelhas", font=(14), bg="white")
        self.label_informativo.grid(row=0, column=0, padx=35, pady=10, sticky='w')

        self.apagar_button = tk.Button(self.new_window, text="Apagar", command=self.apagar_abelha)
        self.apagar_button.place(x=40, y=350, width=100, height=30)

        self.carrega_dados_abelha()

    def carrega_dados_abelha(self):
        cursor.execute("SELECT id, especie, nome_cientifico, localizacao, TO_CHAR(data_aquisicao, 'DD/MM/YYYY') AS data_formatada FROM abelhas")
        rows = cursor.fetchall()

        for i in self.lista_abelhas.get_children():
            self.lista_abelhas.delete(i)

        for row in rows:
            self.lista_abelhas.insert("", "end", values=row)

    def apagar_abelha(self):
        try:
            if not self.lista_abelhas.selection():
                messagebox.showwarning("Aviso", "Por favor, selecione um item para apagar")
            elif messagebox.askokcancel("Confirmação", "Deseja realmente apagar o item selecionado?"):
                for each_item in self.lista_abelhas.selection():
                    id = self.lista_abelhas.item(each_item, 'values')[0]
                    cursor.execute("DELETE FROM caixas WHERE especie_id = %s", (id,))
                    cursor.execute("DELETE FROM abelhas WHERE id = %s", (id,))
                conn.commit()
                self.carrega_dados_abelha()
        except psycopg2.IntegrityError as e:
            messagebox.showwarning("Aviso!", "Não é possível apagar o item selecionado porque ele está relacionado a outros registros.")
            conn.rollback()
        except psycopg2.OperationalError as e:
            messagebox.showwarning("Aviso!", "Erro operacional no banco de dados. Verifique a conexão.")
            conn.rollback()
        except psycopg2.DatabaseError as e:
            messagebox.showwarning("Aviso!", f"Ocorreu um erro no banco de dados: {e}")
            conn.rollback()
        except Exception as e:
            messagebox.showwarning("Aviso!", f"Ocorreu um erro desconhecido: {e}")
            conn.rollback()