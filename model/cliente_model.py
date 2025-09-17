from db.db import get_connection

def criar_tabela_clientes():
    with get_connection() as conexao:
        cursor = conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT,
                email TEXT
            )
        ''')
        conexao.commit()

def adicionar_cliente(nome, telefone, email):
    with get_connection() as conexao:
        cursor = conexao.cursor()
        cursor.execute('''
            INSERT INTO clientes (nome, telefone, email) 
            VALUES (?, ?, ?);
        ''', (nome, telefone, email))
        conexao.commit()
        return cursor.lastrowid

def listar_clientes():
    with get_connection() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, telefone, email FROM clientes;")
        return cursor.fetchall()

def atualizar_cliente(cliente_id, nome, telefone, emnail):
    with get_connection() as conexao:
        cursor = conexao.cursor()
        cursor.execute('''
                       UPDATE clientes 
                       SET nome=?, telefone=?, email=? WHERE id=?;''',
                       (nome, telefone, emnail, cliente_id)
                       )
        conexao.commit()
        return cursor.rowcount

def deletar_cliente(cliente_id):
    with get_connection() as conexao:
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM clientes WHERE id=?", (cliente_id,))
        conexao.commit()
        return cursor.rowcount