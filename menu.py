while True:
    print("\n1 - Somar")
    print("2 - Subtrair")
    print("3 - Tabuada")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        numero = int(input("Digite o primeiro valor: "))
        numero_2 = int(input("Digite o segundo valor: "))
        print("Resultado:", numero + numero_2)

    elif opcao == "2":
        numero = int(input("Digite o primeiro valor: "))
        numero_2 = int(input("Digite o segundo valor: "))
        print("Resultado:", numero - numero_2)

    elif opcao == "3":
        numero = int(input("Digite um número: "))
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero*i}")

    elif opcao == "4":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")