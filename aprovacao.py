nota_1 = float(input("Digite a nota da primeira prova: "))
nota_2 = float(input("Digite a nota da segunda prova: "))
nota_3 = float(input("Digite a nota da terceira prova: "))
media = (nota_1 + nota_2 + nota_3) / 3
print("A média das notas é:", media)
if media >= 7:
    print("Parabéns, você foi aprovado!")
else:
    if media >= 5 and media < 7:
        print("Você está de recuperação.")
    else:
        if media < 5:
            print("Infelizmente, você foi reprovado.")