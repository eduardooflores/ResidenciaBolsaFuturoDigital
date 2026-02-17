flag = True

while flag:
    try:
        numeros = []
        primeiro_valor = int(input("Digite o primeiro valor: "))
        segundo_valor = int(input("Digite o segundo valor: "))

        valor_atual = primeiro_valor
        while valor_atual <= segundo_valor:
            numeros.append(valor_atual)
            valor_atual += 1

        total = sum(numeros)

        print(f"A soma dos valores dentro do intervalo de {primeiro_valor} até {segundo_valor} é: {total}")

        flag = False

    except ValueError:
        print("ERRO! O valor digitado deve ser um número inteiro.")
