soma = 0

print("Números múltiplos de 3 no intervalo de 50 a 125:")

for numero in range(50, 126):
    if numero % 3 == 0:
        print(numero, end=" ")
        soma += numero

print("\n\nSoma dos múltiplos de 3:", soma)
