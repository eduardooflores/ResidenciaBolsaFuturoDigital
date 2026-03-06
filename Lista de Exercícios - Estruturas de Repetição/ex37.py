valores = []

for i in range(10):
    try:
        valor = int(input(f"Digite o {i+1}º valor inteiro: "))
        valores.append(valor)
    except ValueError:
        print("ERRO! O valor digitado deve ser um número inteiro.")

soma_valores = sum(valores)

if soma_valores % 2 == 0:
    valores_pares = [v for v in valores if v % 2 == 0]
    print(f"A soma dos valores é: {soma_valores}")
    print(f"Os valores PARES digitados foram: {valores_pares}")
else:
    valores_impares = [v for v in valores if v % 2 == 1]
    print(f"A soma dos valores é: {soma_valores}")
    print(f"Os valores ÍMPARES digitados foram: {valores_impares}")