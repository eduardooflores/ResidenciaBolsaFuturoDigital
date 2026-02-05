numeros = []
numeros_quadrados = []
numeros_cubos = []

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        numero_quadrado = numero * numero
        numeros_quadrados.append(numero_quadrado)
    else:
        numero_cubo = numero ** 3
        numeros_cubos.append(numero_cubo)

print(f"Quadrado dos números pares: {numeros_quadrados}")
print(f"Cubo dos números ímpares: {numeros_cubos}")