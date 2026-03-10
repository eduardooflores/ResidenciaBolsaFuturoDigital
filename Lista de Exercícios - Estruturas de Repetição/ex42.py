flag = True

while flag:
    try:
        n = int(input("Digite um número inteiro positivo: "))

        soma = 0
        contador = 1

        while contador <= n:
            soma += contador
            contador += 1

        media = soma / n
        print(f"A média dos valores entre 1 e {n} é: {media:.2f}")

        flag = False

    except ValueError:
        print("ERRO! Digite um número inteiro válido.")
