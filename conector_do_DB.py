import conector

def get_db_connection():
    conn = conector.conn
    cursor = conn.cursor()
    return conn, cursor