from conector_do_DB import get_db_connection

def criar_tabelas():
    try:
        conn, cursor = get_db_connection()
        sql_commands = [
            """
            CREATE TABLE IF NOT EXISTS abelhas (
                id SERIAL PRIMARY KEY,
                especie VARCHAR(255),
                nome_cientifico VARCHAR(255),
                localizacao VARCHAR(255),
                data_aquisicao DATE
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS caixas (
                id SERIAL PRIMARY KEY,
                numero_caixa INTEGER,
                especie_id INTEGER,
                material_caixa VARCHAR(255),
                FOREIGN KEY (especie_id) REFERENCES abelhas(id)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS producao_mel (
                id SERIAL PRIMARY KEY,
                quantidade DOUBLE PRECISION,
                data_producao DATE,
                caixa_id INTEGER,
                FOREIGN KEY (caixa_id) REFERENCES caixas(id)
            );
            """
        ]
        
        for command in sql_commands:
            cursor.execute(command)
        conn.commit()

        print("Tabelas criadas com sucesso.")
    except Exception as e:
        print(f"Erro ao criar tabelas: {e}")