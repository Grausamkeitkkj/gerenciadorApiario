import psycopg2
import conector

def criar_tabelas():
    try:
        conn = conector.conn
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS caixas (
                id SERIAL PRIMARY KEY,
                numero_caixa INTEGER,
                especie VARCHAR(255),
                material_caixa VARCHAR(255)
            )
        """)
        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS abelhas (
                            id SERIAL PRIMARY KEY,
                            especie VARCHAR(255),
                            nome_cientifico VARCHAR(255),
                            localizacao VARCHAR(255),
                            data_aquisicao DATE,
                            caixa VARCHAR(255)
                        );
                        """)
        conn.commit()
        print("Tabelas criadas com sucesso.")
    except Exception as e:
        print(f"Erro ao criar tabelas: {e}")