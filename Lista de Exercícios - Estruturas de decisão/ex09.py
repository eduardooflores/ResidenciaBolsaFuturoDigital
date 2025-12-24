n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))
negativos = 0

if n1 < 0:
    negativos += 1

if n2 < 0:
    negativos += 1

if n3 < 0:
    negativos += 1

print(f"Valores negativos: {negativos}")