valor = float(input("Valor do produto: "))

if valor < 100:
    print("Sem desconto")
elif valor <= 299:
    print(f"Valor original: R${valor:.2f}")
    print(f"Desconto: R${valor * 0.05:.2f}")
    print(f"Valor final: R${valor - valor * 0.05:.2f}")
elif valor <= 499:
    print(f"Valor original: R${valor:.2f}")
    print(f"Desconto: R${valor * 0.10:.2f}")
    print(f"Valor final: R${valor- valor * 0.10:.2f}")
else:
    print(f"Valor original: R${valor:.2f}")
    print(f"Desconto: R${valor * 0.15:.2f}")
    print(f"Valor final: R${valor - valor * 0.15:.2f}")

