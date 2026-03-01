valores = []

while True:
    try:
        valor = float(input("Digite um valor ou 0 para sair do programa: "))

        if valor < 0:
            print("Valor não cadastrado! Deve ser maior que zero.")
        elif valor != 0:
            valores.append(valor)
        else:
            break

    except ValueError:
        print("ERRO! Deve digitar um valor numérico.")

# Só calcula se houver valores cadastrados
if valores:
    soma_valores = sum(valores)
    media_valores = soma_valores / len(valores)
    maior_valor = max(valores)
    menor_valor = min(valores)

    print(f"Valores: {valores}")
    print(f"Soma dos valores: {soma_valores}")
    print(f"A média dos valores: {media_valores}")
    print(f"O maior valor: {maior_valor}")
    print(f"O menor valor: {menor_valor}")
else:
    print("Nenhum valor foi cadastrado.")