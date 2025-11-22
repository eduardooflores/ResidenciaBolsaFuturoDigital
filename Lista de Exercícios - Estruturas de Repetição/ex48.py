try:
    numero = int(input("Digite um número inteiro: "))

    saida = " ".join([str(numero)] * numero)

    print(saida)

except:
    print("ERRO! DADOS INVÁLIDOS! DIGITE UM NÚMERO INTEIRO")


