flag = True

while flag:
    try:
        numeros = []
        primeiro_valor = int(input("Digite o primeiro valor: "))
        segundo_valor = int(input("Digite o segundo valor: "))

        for numero in range(primeiro_valor, segundo_valor + 1):
            numeros.append(numero)

        total = sum(numeros)

        print(f"A soma dos valores dentro do intervalo de {primeiro_valor} até {segundo_valor} é: {total}")

        flag = False

    except ValueError:
        print("ERRO! O valor digitado deve ser um número inteiro.")
