valores = []

while True:
    try:
        valor = int(input("Digite um valor ou 0 para sair: "))

        if valor != 0:
            valores.append(valor)
        else:
            break

    except ValueError:
        print("ERRO! O valor digitado deve ser um número inteiro.")

if valores:
    media = sum(valores) / len(valores)

    if media > 30:
        print(f"A média dos valores {valores} é maior que 30!")
    else:
        print(f"A média dos valores {valores} é menor ou igual a 30!")
else:
    print("Nenhum valor foi digitado.")