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