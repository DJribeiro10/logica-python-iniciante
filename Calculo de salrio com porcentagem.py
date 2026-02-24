salario = float(input("Qual e seu salario ? "))
salario1 = float(salario * 0.10)
salario2 = float(salario *0.11)

print (f"salario atual: {salario:.2f}")
print (f"aumento de 10%: {salario1:.2f}")
print (f"Novo salario: {salario1 + salario:.2f}")
print (f"Desconto INSS: {salario2:.2f}")