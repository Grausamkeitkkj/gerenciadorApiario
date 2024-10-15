import os
import psycopg2
import tabelas
from dotenv import load_dotenv
from tkinter import messagebox

load_dotenv()

dbname = os.getenv('DB_NAME')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')

try:
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("Conexão estabelecida com sucesso!")
except Exception as e:
    messagebox.showerror("Erro de Conexão", f"Erro ao conectar ao banco de dados: {e}")
    print("Erro ao conectar ao banco de dados:", e)