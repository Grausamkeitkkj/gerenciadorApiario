import tkinter as tk
from tkinter import ttk, messagebox
from conector_do_DB import get_db_connection
import psycopg2

conn, cursor = get_db_connection()

class TreeviewMel:
    def __init__(self, parent):
        self.parent = parent
        self.new_window = tk.Toplevel(parent)
        self.new_window.title("Cadastro Produção de Mel")
        self.new_window.geometry("825x450")
        self.new_window.configure(background="White")

        self.master = parent
        self.lista_mel = ttk.Treeview(self.new_window, height=3, column=("col1", "col2", "col3", "col4"))
        self.lista_mel.heading("#0", text="")
        self.lista_mel.heading("#1", text="ID")
        self.lista_mel.heading("#2", text="Número da Caixa")
        self.lista_mel.heading("#3", text="Quantidade")
        self.lista_mel.heading("#4", text="Data de Produção")

        self.lista_mel.column("#0", width=0)
        self.lista_mel.column("#1", width=0, stretch=tk.NO)
        self.lista_mel.column("#2", width=100)
        self.lista_mel.column("#3", width=120)
        self.lista_mel.column("#4", width=70)
    
        self.lista_mel.place(x=40, y=40, width=700, height=300)
        
        self.scroolbar = tk.Scrollbar(self.new_window, orient='vertical', command=self.lista_mel.yview)
        self.scroolbar.place(x=740, y=40, height=300)
        self.lista_mel.configure(yscrollcommand=self.scroolbar.set)

        self.label_informativo = tk.Label(self.new_window, text="", font=(14), bg="white")
        self.label_informativo.grid(row=0, column=0, padx=35, pady=10, sticky='w')

        self.apagar_button = tk.Button(self.new_window, text="Apagar Produção", command=self.apagar_producao)
        self.apagar_button.place(x=40, y=350, width=100, height=30)

        self.carrega_dados_producao()

    def carrega_dados_producao(self):
        cursor.execute("SELECT a.id, b.numero_caixa, a.quantidade, TO_CHAR(a.data_producao, 'DD/MM/YYYY') FROM producao_mel a LEFT JOIN caixas b ON a.caixa_id = b.id")
        rows = cursor.fetchall()

        for i in self.lista_mel.get_children():
            self.lista_mel.delete(i)

        for row in rows:
            self.lista_mel.insert("", "end", values=row)

    def apagar_producao(self):
        try:
            if not self.lista_mel.selection():
                messagebox.showwarning("Aviso", "Selecione um item para apagar")
            elif messagebox.askokcancel("Confirmação", "Deseja realmente apagar o item selecionado?"):
                for each_item in self.lista_mel.selection():
                    id = self.lista_mel.item(each_item, 'values')[0]
                    cursor.execute("DELETE FROM producao_mel WHERE id = %s", (id,))
                    conn.commit()
                    self.carrega_dados_producao()
        except psycopg2.IntegrityError as e:
            messagebox.showerror("Erro", "Não é possível apagar o item selecionado porque ele está relacionado a outros registros.")
            conn.rollback()
        except psycopg2.OperationalError as e:
            messagebox.showerror("Erro", "Erro operacional no banco de dados. Verifique a conexão.")
            conn.rollback()
        except psycopg2.DatabaseError as e:
            messagebox.showerror("Erro", f"Ocorreu um erro no banco de dados: {e}")
            conn.rollback()
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro desconhecido: {e}")
            conn.rollback()
