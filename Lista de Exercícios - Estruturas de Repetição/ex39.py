valores = []
valores_impares = []

for i in range(10):
    try:
        valor = int(input(f"Digite o {i+1}º número inteiro: "))
        valores.append(valor)

        if valor % 2 == 1:
            valores_impares.append(valor)
    except ValueError:
        print("ERRO! O valor digitado deve ser um número inteiro.")

if valores_impares:
    media_numeros_impares = sum(valores_impares) / len(valores_impares)
    print(f"A média dos valores ímpares é: {media_numeros_impares:.2f}")
else:
    print("Nenhum número ímpar foi digitado.")
