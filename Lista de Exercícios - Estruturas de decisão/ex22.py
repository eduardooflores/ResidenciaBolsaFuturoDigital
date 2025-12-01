# ENTRADA
salario_bruto = float(input("Digite seu salário bruto: "))
valor_prestacao = float(input("Digite o valor da prestação: "))

# PROCESSAMENTO
porcentagem_30_salario_bruto = salario_bruto * 0.30

if valor_prestacao > porcentagem_30_salario_bruto:
    print("O empréstimo não pode ser concedido")
else:
    print("O empréstimo pode ser concedido")