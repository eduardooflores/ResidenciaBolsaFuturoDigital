n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma = n1 + n2
multiplicacao = n1 * n2

if multiplicacao < 75:
    print(f"Valor do primeiro número: {n1}")
    print(f"Valor do segundo número: {n2}")
    print(f"A soma dos valores é {soma}")
else:
    print(f"Valor do primeiro número: {n1}")
    print(f"Valor do segundo número: {n2}")
    print(f"A multiplicação dos valores é: {multiplicacao}")