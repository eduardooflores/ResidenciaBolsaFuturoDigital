numeros_impares = []

for numero in range(10, 51):
    if numero % 2 == 1:
        numeros_impares.append(numero)

print(f"Números Ímpares entre 10 e 50: {numeros_impares}")