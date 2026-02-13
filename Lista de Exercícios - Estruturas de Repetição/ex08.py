numeros_impares = []

for numero in range (50, 4, -1):
    if numero % 2 == 1:
        numeros_impares.append(numero)
    print(numero)
print(f"Os números ímpares de 50 até 5 são? {numeros_impares}")