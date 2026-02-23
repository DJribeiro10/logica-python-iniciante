nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
ano_atual = int(input("Digite o ano atual: "))

quantos_anos_faltam_para_50 = 50 - idade
ano_final = ano_atual + quantos_anos_faltam_para_50


print("Olá", nome)
print("em ", ano_final, "você terá 50 anos")