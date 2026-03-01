# Exercício 1
numero = 100
while numero <= 300:
    if numero % 5 == 0 or numero % 6 == 0:
        print(numero)
    numero += 1


# Exercício 2
numero = 10
while numero <= 150:
    if numero % 3 == 0 or numero % 7 == 0:
        print(numero)
    numero += 1


# Exercício 3
print("Números múltiplos de 5 no intervalo de 20 a 100:")

numero = 20
while numero <= 100:
    if numero % 5 == 0:
        print(numero, end=" ")
    numero += 1


# Exercício 4
soma = 0
print("Números múltiplos de 3 no intervalo de 50 a 125:")

numero = 50
while numero <= 125:
    if numero % 3 == 0:
        print(numero, end=" ")
        soma += numero
    numero += 1

print("\n\nSoma dos múltiplos de 3:", soma)


# Exercício 5
numeros = []
numero = 19
while numero < 120:
    numeros.append(numero)
    numero += 8

soma = sum(numeros)
print(f"A soma dos números de 19 até 119 é: {soma}")
