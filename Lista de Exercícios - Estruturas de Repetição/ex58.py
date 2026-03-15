for i in range(10):
    try:
        valor = int(input(f"Digite o {i+1}º número inteiro: "))
        if valor:
            antecessor = valor - 1
            sucessor = valor + 1
            print(f"O valor digitado foi: {valor}")
            print(f"O antecessor do valor é: {antecessor}")
            print(f"O sucessor do valor é: {sucessor}")
    except ValueError:
        print("ERRO! Digite um número inteiro.")