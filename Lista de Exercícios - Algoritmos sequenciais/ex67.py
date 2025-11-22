#  Questão 67. Antes de o racionamento de energia ser decretado, quase ninguém falava em
# quilowatts; mas, agora, todos incorporaram essa palavra em seu vocabulário. Sabe-se que
# 100quilowatss de energia custa um sétimo do salário mínimo, fazer um algoritmo que receba o valor
# do salário mínimo e a quantidade de quilowatts gasta por uma residência e calcule. Imprima:
# • o valor em reais de cada quilowatts
# • o valor em reais a ser pago
# • o novo valor a ser pago por essa residência com um desconto de 10%

# ENTRADA
DESCONTO = 0.10

salario_minimo = float(input("Digite o salário mínimo: "))
qntd_quilowatts = float(input("Digite a quantidade de quilowatts gasta na residência: "))

# PROCESSAMENTO
valor_quilowatts = (salario_minimo / 7) / 100
total_valor_quilowatts = valor_quilowatts * qntd_quilowatts
total_desconto = total_valor_quilowatts * (1 - DESCONTO)

# SAÍDA
print(f"Valor de cada quilowatt: R$ {valor_quilowatts:.2f}")
print(f"Valor total a ser pago: R$ {total_valor_quilowatts:.2f}")
print(f"Valor com 10% de desconto: R$ {total_desconto:.2f}")