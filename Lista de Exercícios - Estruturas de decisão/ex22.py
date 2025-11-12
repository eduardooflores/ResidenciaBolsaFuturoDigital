# Questão 22. A prefeitura de Porto Alegre abriu uma linha de crédito para os funcionários
# estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário bruto. Elabore
# um algoritmo que permita entrar com o salário bruto e o valor da prestação e informar se o
# empréstimo pode ou não ser concedido.


# ENTRADA
salario_bruto = float(input("Digite seu salário bruto: "))
valor_prestacao = float(input("Digite o valor da prestação: "))

# PROCESSAMENTO
porcentagem_30_salario_bruto = salario_bruto * 0.30

if valor_prestacao > porcentagem_30_salario_bruto:
    print("O empréstimo não pode ser concedido")
else:
    print("O empréstimo pode ser concedido")