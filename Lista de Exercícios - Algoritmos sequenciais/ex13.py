# Questão 13. Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são
# descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa
# que nos dê: salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato. o salário líquido. calcule
# os descontos e o salário líquido, conforme a tabela abaixo: + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

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