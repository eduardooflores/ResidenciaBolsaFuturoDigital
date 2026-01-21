valor_hora = float(input("Digite o valor da sua hora: "))
horas_trabalhadas = float(input("Digite as horas trabalhadas: "))

salario_bruto = valor_hora * horas_trabalhadas

if horas_trabalhadas > 40:
    salario_bruto *= 2  #
    print(f"O salário bruto para {horas_trabalhadas} horas trabalhadas é de: R${salario_bruto:.2f}")
else:
    print(f"O salário bruto para {horas_trabalhadas} horas trabalhadas é de: R${salario_bruto:.2f}")
