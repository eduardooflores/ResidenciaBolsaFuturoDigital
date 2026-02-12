numeros_impares = []

for numero in range(20, 51):
    if numero % 2 == 1:
        numeros_impares.append(numero)

soma_impares = sum(numeros_impares)
qntd_numeros = len(numeros_impares)

print(f"A soma dos números pares de 1 até 50 é: {soma_impares}")
print(f"Foram utilizados {qntd_numeros} números para calcular a soma")