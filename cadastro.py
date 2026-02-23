cadastros = []

while True:
    print("\n1 - Cadastrar pessoa")
    print("2 - Listar cadastros")
    print("3 - Excluir cadastro")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))

        pessoa = {"nome": nome, "idade": idade}
        cadastros.append(pessoa)

        print(f"{nome} cadastrado com sucesso!")

    elif opcao == "2":
        print("\nLista de cadastros:")
        for pessoa in cadastros:
            print(f"{pessoa['nome']} - {pessoa['idade']} anos")

    elif opcao == "3":
        nome = input("Digite o nome da pessoa a ser excluída: ")
        cadastros = [pessoa for pessoa in cadastros if pessoa['nome'] != nome]
        print(f"{nome} excluído com sucesso!")

    elif opcao == "4":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")