def verificar_pagamento(saldo, divida):
    divida_3 = divida * 1.03
    divida_5 = divida * 1.05

    if saldo < divida:
        return "A dívida não pode ser paga"
    elif saldo >= divida_5:
        return "Saldo suficiente para pagar em qualquer dia"
    elif saldo >= divida_3:
        return "Saldo suficiente para pagar até o dia 20"
    else:
        return "Saldo suficiente para pagar até o dia 10"


saldo = float(input("Digite o saldo disponível: "))
divida = float(input("Digite o valor da dívida: "))

mensagem = verificar_pagamento(saldo, divida)
print(mensagem)
