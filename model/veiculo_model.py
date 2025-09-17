from db.db import get_connection

def criar_tabela_veiculos():
    with get_connection() as conexao:
        cursor = conexao.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS veiculos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            modelo TEXT NOT NULL,
            placa TEXT UNIQUE NOT NULL,
            ano INTEGER,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id) 
        );
        ''')
        conexao.commit()

def adicionar_veiulo(cliente_id, modelo, placa, ano):
    with get_connection() as conexao:
        cursor = conexao.cursor()
        cursor.execute('''
            INSERT INTO veiculos (cliente_id, modelo, placa, ano)
            VALUES (?, ?, ?, ?);
        ''', (cliente_id, modelo, placa, ano))
        conexao.commit()
        return cursor.lastrowid

def listar_veiculos():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT v.id, v.modelo, v.placa, v.ano, c.nome
        FROM veiculos v
        JOIN clientes c ON v.cliente_id = c.id;
        """)
        return cursor.fetchall()