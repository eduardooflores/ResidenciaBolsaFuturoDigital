numeros = []

for i in range(5):
    try:
        numero = int(input(f"Digite o {i+1}º número inteiro: "))
        numeros.append(numero)

    except ValueError:
        print("ERRO! Digite apenas números inteiros.")

for numero in numeros:
    quadrado = numero ** 2
    print(quadrado)