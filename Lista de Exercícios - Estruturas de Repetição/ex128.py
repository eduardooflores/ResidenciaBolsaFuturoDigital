try:
    n = int(input("Digite a quantidade de números: "))

    maior = None

    for i in range(n):
        try:
            valor = int(input(f"Digite o {i+1}º número: "))
            triplo = valor * 3
            print(f"{valor} - {triplo}")

            if maior is None or valor > maior:
                maior = valor
        except ValueError:
            print("ERRO! Digite apenas números inteiros.")
            i -= 1

    if maior is not None:
        print(f"Maior: {maior} - {maior * 3}")
    else:
        print("Nenhum número válido foi digitado.")

except ValueError:
    print("ERRO! A quantidade de números deve ser um valor inteiro.")
