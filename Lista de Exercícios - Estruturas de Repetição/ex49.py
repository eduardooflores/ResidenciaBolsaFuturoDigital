flag = True

while flag:
    try:
        numero = int(input("Digite um número inteiro: "))

        saida = " ".join([str(numero)] * numero)

        print(saida)

        continua = int(input("Deseja adicionar outro valor (1.Sim 2.Não)?"))
        if continua == 1:
            continue
        elif continua == 2:
            flag = False
        else:
            print("Dados inválidos, digite 1 ou 2")
    except:
        print("ERRO! DADOS INVÁLIDOS! DIGITE UM NÚMERO INTEIRO")


