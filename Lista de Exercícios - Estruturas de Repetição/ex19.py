try:
    valor = int(input("Digite um número inteiro maior que 100: "))

    if valor <= 100:
        print("Valor inválido! O número deve ser maior que 100.")
    else:
        soma_pares = 0
        produto_impares = 1

        for num in range(100, valor + 1):
            if num % 2 == 0:
                soma_pares += num
            else:
                produto_impares *= num

        print("Soma dos valores pares:", soma_pares)
        print("Produto dos valores ímpares:", produto_impares)

except ValueError:
    print("Entrada inválida! Digite apenas números inteiros.")
