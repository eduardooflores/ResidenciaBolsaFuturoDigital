valores = []
valores_maior_que_20 = []

for i in range(8):
    try:
        valor = int(input(f"Digite o {i+1}º valor inteiro: "))
        valores.append(valor)
    except ValueError:
        print("ERRO! O valor digitado deve ser um número inteiro.")

soma_valores = sum(valores)

for valor in valores:
    if valor > 20:
        valores_maior_que_20.append(valor)

print(f"A soma dos valores é: {soma_valores}")

if valores_maior_que_20:
    media_valores = sum(valores_maior_que_20) / len(valores_maior_que_20)
    print(f"A média dos valores maiores que 20 é: {media_valores}")
else:
    print("Não há valores maiores que 20, portanto não é possível calcular a média.")
