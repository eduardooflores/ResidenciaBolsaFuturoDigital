numeros_pares = []

for numero in range(1,51):
    if numero % 2 == 0:
        numeros_pares.append(numero)

soma_pares = sum(numeros_pares)
qntd_numeros = len(numeros_pares)

print(f"A soma dos números pares de 1 até 50 é: {soma_pares}")
print(f"Foram utilizados {qntd_numeros} números para calcular a soma")