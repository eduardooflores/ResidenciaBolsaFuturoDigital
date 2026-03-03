try:
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    try:
        soma = valor1 + valor2
        subtracao = valor1 - valor2
        multiplicacao = valor1 * valor2
        divisao = valor1 / valor2

        print(f"SOMA dos valores: {soma:.2f}")
        print(f"SUBTRAÇÃO dos valores: {subtracao:.2f}")
        print(f"MULTIPLICAÇÃO dos valores: {multiplicacao:.2f}")
        print(f"DIVISÃO dos valores: {divisao:.2f}")

    except ZeroDivisionError:
        print("ERRO! Divisão por zero não pode ser efetuada.")

except ValueError:
    print("ERRO! Os valores devem ser numéricos.")
