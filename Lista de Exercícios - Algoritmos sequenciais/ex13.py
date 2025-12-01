valor_hora = float(input("Digite o quanto você ganha por hora: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mes: "))

salario_bruto = valor_hora * horas_trabalhadas

DESCONTO_INSS = 0.05
DESCONTO_IR = 0.11
DESCONTO_SINDICATO = 0.05

valor_desconto_inss = salario_bruto * DESCONTO_INSS
valor_desconto_ir = salario_bruto * DESCONTO_IR
valor_desconto_sindicato = salario_bruto * DESCONTO_SINDICATO

salario_liquido = salario_bruto - valor_desconto_inss - valor_desconto_ir - valor_desconto_sindicato

print(f"O seu salário bruto é de: R${salario_bruto}; Valor pago de INSS é de: R${valor_desconto_inss}; "
      f"Valor pago de IR é de: R${valor_desconto_ir}; Valor pago sindicato é de: R${valor_desconto_sindicato}"
      f"Valor salário líquido é de: R${salario_liquido}")