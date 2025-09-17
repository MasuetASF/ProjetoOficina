import sqlite3

# Nome do arquivo do banco
import os

DB_PATH = os.path.join(os.path.dirname(__file__),"..", "auto_service.db")

# 🔹 Função para abrir conexão (usada pelos models)
def get_connection():
    return sqlite3.connect(DB_PATH)

# 🔹 Inicializar todas as tabelas
def inicializar_banco():
    from model.cliente_model import criar_tabela_clientes
    from model.veiculo_model import criar_tabela_veiculos
    from model.ordem_model import criar_tabela_ordens

    criar_tabela_clientes()
    criar_tabela_veiculos()
    criar_tabela_ordens()
    print("Banco inicializado com sucesso!")
    print(DB_PATH)