import psycopg2
import conector

def criar_tabelas():
    conn = conector.conn
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS caixas (
            id_caixa SERIAL PRIMARY KEY,
            nome_caixa VARCHAR(50) NOT NULL,
            tipo_caixa VARCHAR(50) NOT NULL,
            data_aquisicao DATE NOT NULL,
            data_instalacao DATE NOT NULL,
            data_retirada DATE
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS caixas_abelhas (
            id_caixa_abelha SERIAL PRIMARY KEY,
            id_caixa INTEGER NOT NULL,
            id_abelha INTEGER NOT NULL
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Tabela caixas criada com sucesso!")