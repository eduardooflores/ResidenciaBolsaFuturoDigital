# Q uestão 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input("Digite o quanto você ganha por hora: "))
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas no mes: "))

salario = valor_hora * horas_trabalhadas

print(f"O total de salári bruto a receber é de: {salario}")