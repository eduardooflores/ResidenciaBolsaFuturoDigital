print("Números múltiplos de 5 no intervalo de 20 a 100:")

for numero in range(20, 101):
    if numero % 5 == 0:
        print(numero, end=" ")
