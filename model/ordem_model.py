from db.db import get_connection

def criar_tabela_ordens():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ordens_servico (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_id INTEGER NOT NULL,
                veiculo_id INTEGER NOT NULL,
                descricao TEXT NOT NULL,
                status TEXT DEFAULT 'aberta',
                valor REAL,
                data_abertura DATE DEFAULT CURRENT_DATE,
                data_fechamento DATE,
                FOREIGN KEY (cliente_id) REFERENCES clientes(id),
                FOREIGN KEY (veiculo_id) REFERENCES veiculos(id)
            );
        """)
        conn.commit()

def adicionar_ordem(cliente_id, veiculo_id, descricao, valor=None):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO ordens_servico (cliente_id, veiculo_id, descricao, valor)
            VALUES (?, ?, ?, ?)
        """, (cliente_id, veiculo_id, descricao, valor))
        conn.commit()
        return cursor.lastrowid

def listar_ordens():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT o.id, c.nome, v.modelo, v.placa, o.descricao, o.status, o.valor, o.data_abertura, o.data_fechamento
            FROM ordens_servico o
            JOIN clientes c ON o.cliente_id = c.id
            JOIN veiculos v ON o.veiculo_id = v.id
        """)
        return cursor.fetchall()
