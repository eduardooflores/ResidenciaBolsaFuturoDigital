contador_par = 0
contador_impar = 0
contador_positivo = 0
contador_negativo = 0
numeros = []

for i in range(10):
    numero = int(input("Digite um valor: "))
    numeros.append(numero)

    if numero % 2 == 0:
        contador_par += 1
    else:
        contador_impar += 1

    if numero >= 0:
        contador_positivo += 1
    else:
        contador_negativo += 1

print(f"Na lista de números inseridos {numeros} existem:")
print(f"{contador_par} números pares.")
print(f"{contador_impar} números ímpares.")
print(f"{contador_positivo} números positivos.")
print(f"{contador_negativo} números negativos.")
