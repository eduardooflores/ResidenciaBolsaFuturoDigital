numeros = []
numeros_negativos = 0
numeros_intervalo = 0
numeros_maior_100 = 0

for i in range(15):
    try:
        numero = int(input(f"Digite {i+1}º número: "))
        numeros.append(numero)

    except ValueError:
        print("ERRO! Digite um número inteiro.")

for numero in numeros:
    if numero < 0:
        numeros_negativos += 1
    elif numero >= 15 and numero <= 45:
        numeros_intervalo += 1
    elif numero > 100:
        numeros_maior_100 += 1

print(f"Quantidade de números negativos: {numeros_negativos}")
print(f"Quantidade de números entre o intervalo de 15 até 45: {numeros_intervalo}")
print(f"Quantidade de números maiores que 100: {numeros_maior_100}")