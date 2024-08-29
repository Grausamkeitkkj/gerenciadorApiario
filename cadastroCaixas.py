import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from conector_do_DB import get_db_connection

conn, cursor = get_db_connection()

class cadastroCaixas:
    def __init__(self, parent):
        self.parent = parent
        self.new_window = tk.Toplevel(parent)
        self.new_window.title("Cadastro de Caixas")
        self.new_window.geometry("400x300")
        self.new_window.configure(background="White")
        self.opcoes = []
        self.carrega_dados_combobox()

        self.numero_caixa_label = tk.Label(self.new_window, background="White", text="Número da Caixa:")
        self.numero_caixa_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.numero_caixa_entry = tk.Entry(self.new_window)
        self.numero_caixa_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.especie_label = tk.Label(self.new_window, background="White", text="Espécie:")
        self.especie_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        self.especie_entry = ttk.Combobox(self.new_window, values=self.opcoes)
        self.especie_entry.grid(row=1, column=1, padx=10, pady=10)
        self.especie_entry.set("Selecione a espécie")

        self.material_caixa_label = tk.Label(self.new_window, background="White", text="Material da Caixa:")
        self.material_caixa_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.material_caixa_entry = tk.Entry(self.new_window)
        self.material_caixa_entry.grid(row=2, column=1, padx=10, pady=10)

        self.salvar_button = tk.Button(self.new_window, text="Salvar", command=lambda:[self.salva_dados_caixa()])
        self.salvar_button.grid(row=4, column=0, columnspan=2, padx=36, pady=10)
        self.salvar_button.place(relx=0.5, rely=0.9,relwidth=0.50, relheight=0.15, anchor='center')

    def salva_dados_caixa(self):
        numero_caixa = self.numero_caixa_entry.get()
        especie = self.especie_entry.get()
        material_caixa = self.material_caixa_entry.get()
    
        try:
            numero_caixa_int = int(numero_caixa)
        except ValueError:
            messagebox.showwarning("Aviso", "Número da Caixa deve ser um número")
            return
    
        if numero_caixa_int <= 0:
            messagebox.showwarning("Aviso", "Número da Caixa deve ser um número maior que 0")  
    
        if not numero_caixa or not especie or not material_caixa:
            messagebox.showwarning("Aviso","Por favor, complete todos os campos antes de salvar")
        else:
            cursor.execute("SELECT id FROM abelhas WHERE especie = %s", (especie,))
            abelha_id = cursor.fetchone()
    
            if abelha_id:
                cursor.execute("INSERT INTO caixas (numero_caixa, especie_id, material_caixa) VALUES (%s, %s, %s)",
                               (numero_caixa, abelha_id[0], material_caixa))
                conn.commit()
                messagebox.showinfo("Aviso","Dados salvos com sucesso")
                self.numero_caixa_entry.delete(0, tk.END)
                self.especie_entry.delete(0, tk.END)
                self.material_caixa_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Aviso", "Espécie não encontrada.")
    def carrega_dados_combobox(self):
        cursor.execute("SELECT especie FROM abelhas")
        rows = cursor.fetchall()
        for row in rows:
            self.opcoes.append(row[0])