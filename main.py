from data.database import criar_tabela
from vendas import (
    popular_dados_iniciais
)

import middleware as fun

criar_tabela()

def menu ():
    while True: 
            print("\n" + "=" * 30)
            print("      MENU PRINCIPAL       ")
            print("=" * 30)
            print("1. Cadastrar Venda")
            print("2. Buscar Venda")
            print("3. Listar Venda")
            print("4. Atualizar venda")
            print("5. Deletar Venda")
            print("6. Sair")
            print("=" * 30)

            opcao = input("Escolha uma opção (1-6): ").strip()

            if opcao == "1":
                fun.adicionar_venda()
            elif opcao == "2":
                fun.buscarPorId()
            elif opcao == "3":
                fun.listar()
            elif opcao == "4":
                fun.editar()
            elif opcao == "5":
                fun.deletar()
            elif opcao == "6":
                print("\nSaindo do sistema... Até logo!")
                break
            else:
                print("\nOpção inválida! Escolha um número de 1 a 10.")
                
popular_dados_iniciais()
menu()
