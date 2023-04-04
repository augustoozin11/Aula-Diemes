lista_de_compras = []

while True:
    print("Escolha uma opção:")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Listar itens")
    print("4 - Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        item = input("Digite o nome do item que deseja adicionar: ")
        lista_de_compras.append(item)
        print(f"{item} foi adicionado à lista de compras.")

    elif escolha == "2":
        item = input("Digite o nome do item que deseja remover: ")
        if item in lista_de_compras:
            lista_de_compras.remove(item)
            print(f"{item} foi removido da lista de compras.")
        else:
            print(f"{item} não está na lista de compras.")

    elif escolha == "3":
        print("Itens na lista de compras:")
        for item in lista_de_compras:
            print(item)

    elif escolha == "4":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")