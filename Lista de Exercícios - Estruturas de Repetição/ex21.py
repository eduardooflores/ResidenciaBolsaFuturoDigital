numeros_pares = []

for numero in range(1, 22):
    print(numero)

    if numero % 2 == 0:
        numeros_pares.append(numero)

    soma_pares = sum(numeros_pares)

print(f"A soma dos valores pares entre 1 e 21 é: {soma_pares}")