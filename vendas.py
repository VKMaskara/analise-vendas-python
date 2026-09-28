from data.database import conectar
conn = conectar()

class Vendas:

    def __init__(self, data_venda, produto, categoria, valor_venda, id_venda=None):
        self.id_venda = id_venda
        self.data_venda = data_venda
        self.produto = produto
        self.categoria = categoria
        self.valor_venda = valor_venda

    def __repr__(self):
        return (
            f"Vendas("
            f"id={self.id_venda}, "
            f"{self.data_venda}, "
            f"{self.produto}, "
            f"{self.categoria}, "
            f"{self.valor_venda})"
        )


def registrar_venda(venda):

    cursor = conn.cursor()

    insert = '''
    INSERT INTO vendas1 (
        data_venda,
        produto,
        categoria,
        valor_venda
    )
    VALUES (?, ?, ?, ?)
    '''

    dados = (
        venda.data_venda,
        venda.produto,
        venda.categoria,
        venda.valor_venda
    )

    cursor.execute(insert, dados)

    venda.id_venda = cursor.lastrowid

    conn.commit()


    return venda


def buscar_venda(id_venda):
    cursor = conn.cursor()

    comando_select = "SELECT * FROM vendas1 WHERE id_venda = ?"

    cursor.execute(comando_select, (id_venda,))

    return cursor.fetchone()

def listar_vendas():
    cursor = conn.cursor()

    comando_select = "SELECT * FROM vendas1"

    cursor.execute(comando_select)

    vendas = cursor.fetchall()

    print("Todas Vendas:")

    for venda in vendas:
        print(venda)


def atualizar_venda(id_venda,nova_data, novo_produto, nova_categoria, novo_valor):
    cursor = conn.cursor()
    
    # 3. Comando SQL para atualizar na tabela 'vendas1'
    comando_update = """
    UPDATE vendas1
    SET data_venda = ?, produto = ?, categoria = ?, valor_venda = ?
    WHERE id_venda = ?
    """
    # 4. Executa e guarda as alterações
    cursor.execute(
        comando_update,
        (nova_data, novo_produto, nova_categoria, novo_valor, id_venda)
    )

    conn.commit()

    print("Venda atualizada com sucesso!")


def deletar_venda(id_venda):
    cursor = conn.cursor()  # Adicionados os parênteses ()
    
    # Nome da tabela e da coluna corrigidos
    dellVenda = "DELETE FROM vendas1 WHERE id_venda = ?"
    
    cursor.execute(dellVenda, (id_venda,))
    conn.commit()
    
    print(f"Venda com ID {id_venda} deletada com sucesso!")


# DADOS INICIAIS --------

vendas_iniciais = [
    ('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
    ('2023-01-05', 'Produto B', 'Roupas', 350.00),
    ('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
    ('2023-03-15', 'Produto D', 'Livros', 200.00),
    ('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
    ('2023-04-02', 'Produto F', 'Roupas', 400.00),
    ('2023-05-05', 'Produto G', 'Livros', 150.00),
    ('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
    ('2023-07-20', 'Produto I', 'Roupas', 600.00),
    ('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
    ('2023-09-30', 'Produto K', 'Livros', 300.00),
    ('2023-10-05', 'Produto L', 'Roupas', 450.00),
    ('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
    ('2023-12-20', 'Produto N', 'Livros', 250.00)
]

def popular_dados_iniciais():
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM vendas1")

    # Só insere se a tabela estiver vazia, evitando duplicar os dados
    if cursor.fetchone()[0] > 0:
        print("Banco já possui dados. Carga inicial ignorada.")
        return

    for item in vendas_iniciais:
        venda = registrar_venda(Vendas(*item))
        print(f"{venda.produto} cadastrada com sucesso!")
    