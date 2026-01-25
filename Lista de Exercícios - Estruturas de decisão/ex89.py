numeros = []

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

maior_numero = max(numeros)
menor_numero = min(numeros)

print(f"O maior número digitado foi: {maior_numero}")
print(f"O menor número digitado foi: {menor_numero}")
