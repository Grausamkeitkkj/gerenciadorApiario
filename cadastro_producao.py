import tkinter as tk
from conector_do_DB import get_db_connection
import tkcalendar
from tkinter import messagebox
from tkinter import ttk
import datetime

class CadastroProducao:
    def __init__(self, parent):
        self.parent = parent
        self.new_window = tk.Toplevel(parent)
        self.new_window.title("Cadastro de Produção de Mel")
        self.new_window.geometry("400x300")
        self.new_window.configure(background="White")

        self.quantidade_mel_label = tk.Label(self.new_window, background="White", text="Quantidade de Mel:")
        self.quantidade_mel_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.quantidade_mel_entry = tk.Entry(self.new_window)
        self.quantidade_mel_entry.grid(row=0, column=1, padx=10, pady=10)

        self.data_producao_label = tk.Label(self.new_window, background="White", text="Data de Produção:")
        self.data_producao_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.data_producao_datepicker = tkcalendar.DateEntry(self.new_window, date_pattern='dd/mm/yyyy', locale='pt_BR')
        self.data_producao_datepicker.grid(row=1, column=1, padx=10, pady=10)