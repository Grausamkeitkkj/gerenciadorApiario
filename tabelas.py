import psycopg2
import conector

def criar_tabelas():
    try:
        conn = conector.conn
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS caixas (
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS abelhas (
            );
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("Tabelas criadas com sucesso.")
    except Exception as e:
        print(f"Erro ao criar tabelas: {e}")