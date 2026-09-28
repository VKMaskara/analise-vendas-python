# Este arquivo tem a responsabilidade de gerenciar o banco de dados
import os
import sqlite3
from datetime import date

def conectar():
    # Obtém o caminho do diretório atual (pasta 'data')
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, "dados_vendas.db")
    # Conecta usando o caminho completo e absoluto
    return sqlite3.connect(DB_PATH)





hoje = date.today()

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    create_table = '''
    CREATE TABLE IF NOT EXISTS vendas1 (
        id_venda INTEGER PRIMARY KEY,
        data_venda DATE,
        produto TEXT,
        categoria TEXT,
        valor_venda REAL
    )
    '''
    
    cursor.execute(create_table)
    conn.commit()


