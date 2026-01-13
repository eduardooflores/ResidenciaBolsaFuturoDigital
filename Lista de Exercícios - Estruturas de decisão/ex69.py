conta_corrente = float(input("Digite o saldo da conta corrente: "))
poupanca = float(input("Digite o saldo da conta poupança: "))


if conta_corrente > 1000 or poupanca > 1000:
    if conta_corrente > poupanca:
        valor_conta_especial_dobro = conta_corrente * 2
    else:
        valor_conta_especial_dobro = poupanca * 2

    if conta_corrente < poupanca:
        valor_conta_especial_triplo = conta_corrente * 3
    else:
        valor_conta_especial_triplo = poupanca * 3

    if valor_conta_especial_dobro > valor_conta_especial_triplo:
        print(f"O valor limite da conta especial é: {valor_conta_especial_dobro}")
    else:
        print(f"O valor limite da conta especial é: {valor_conta_especial_triplo}")
else:
    print("SEM CONTA ESPECIAL")