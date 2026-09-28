from vendas import (
    Vendas,
    registrar_venda,
    buscar_venda,
    listar_vendas,
    atualizar_venda,
    deletar_venda
)
from datetime import date
hoje = date.today()

def adicionar_venda():
    data = hoje
    produto = input("nome do produto:")
    categoria = input("Categoria:")
    valor_venda = float(input("Valor da venda:"))
    
    objVenda = Vendas(data, produto, categoria, valor_venda)
    
    registrar_venda(objVenda)

def buscarPorId():
    id_venda = int(input('Buscar por id:'))
        
    resultado = buscar_venda(id_venda)
    
    print(resultado)
    
def listar():
    listar_vendas()
    
def editar():
    id_venda = int(input('Editar por id:'))
    # 1. Busca a venda existente
    venda_edit = buscar_venda(id_venda)
    
    if not venda_edit:
        print(f"Venda com ID {id_venda} não encontrada.")
        return
    
    print(f"Venda atual: {venda_edit}")
        # 2. Solicita as novas informações ao utilizador
    nova_data = input("Nova data (AAAA-MM-DD): ")
    novo_produto = input("Novo produto: ")
    nova_categoria = input("Nova categoria: ")
    novo_valor = float(input("Novo valor da venda: "))
     
    atualizar_venda(id_venda, nova_data, novo_produto, nova_categoria, novo_valor)

def deletar():
    id_venda = int(input('Deletar por id:'))
    
    deletar_venda(id_venda)