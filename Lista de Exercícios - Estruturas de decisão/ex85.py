numeros = []

for i in range(3):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

maior_numero = max(numeros)
print(f"O maior número é: {maior_numero}")