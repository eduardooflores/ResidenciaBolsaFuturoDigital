numeros = []

for i in range(3):
    try:
        numero = int(input(f"Digite o {i+1}º número inteiro: "))
        numeros.append(numero)

    except ValueError:
        print("ERRO! Apenas números inteiros são aceitos.")

if numeros:
    maior_numero = max(numeros)
    print(f"O maior número digitado foi: {maior_numero}")
else:
    print(f"Nenhum número foi digitado.")