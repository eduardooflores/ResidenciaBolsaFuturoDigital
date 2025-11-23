ano_atual = 2025

mais_antigo_nome = None
mais_antigo_ano = None

maior_salario_fem = 0
nome_maior_salario_fem = None

total_salarios_liquidos = 0
total_funcionarios = 0

masc_menor27_salario_menor1700 = 0
total_masc = 0

fem_dependentes_maior3 = 0
total_fem = 0

flag = True
while flag:
    print("\n--- Cadastro de Funcionário ---")
    matricula = input("Matrícula: ")
    nome = input("Nome: ")
    sexo = int(input("Sexo (1-Feminino, 2-Masculino): "))
    salario_bruto = float(input("Salário bruto: R$"))
    dependentes = int(input("Número de dependentes: "))
    ano_nasc = int(input("Ano de nascimento: "))
    ano_ingresso = int(input("Ano de ingresso na empresa: "))

    desconto_inss = salario_bruto * 0.12

    if salario_bruto <= 1500:
        desconto_ir = 0
    elif salario_bruto <= 2700:
        desconto_ir = salario_bruto * 0.15
    elif salario_bruto <= 4700:
        desconto_ir = salario_bruto * 0.275
    else:
        desconto_ir = salario_bruto * 0.35

    salario_liquido = salario_bruto - desconto_inss - desconto_ir + (dependentes * 14)

    total_funcionarios += 1
    total_salarios_liquidos += salario_liquido

    if mais_antigo_ano is None or ano_ingresso < mais_antigo_ano:
        mais_antigo_ano = ano_ingresso
        mais_antigo_nome = nome

    if sexo == 1:
        total_fem += 1
        if salario_liquido > maior_salario_fem:
            maior_salario_fem = salario_liquido
            nome_maior_salario_fem = nome
        if dependentes > 3:
            fem_dependentes_maior3 += 1

    idade = ano_atual - ano_nasc
    if sexo == 2:
        total_masc += 1
        if idade < 27 and salario_liquido < 1700:
            masc_menor27_salario_menor1700 += 1

    # deseja continuar?
    op = input("\nDeseja cadastrar outro funcionário? (S/N): ").upper()
    if op != "S":
        flag = False

percent_masc_menor27_salario_menor1700 = (masc_menor27_salario_menor1700 / total_masc * 100) if total_masc > 0 else 0
percent_fem_dependentes_maior3 = (fem_dependentes_maior3 / total_fem * 100) if total_fem > 0 else 0

print("\n--- RESULTADOS ---")
print(f"a) Funcionário mais antigo: {mais_antigo_nome}")
print(f"b) Funcionária com maior salário líquido: {nome_maior_salario_fem}")
print(f"c) % de homens <27 anos e salário <1700: {percent_masc_menor27_salario_menor1700:.2f}%")
print(f"d) Soma dos salários líquidos da empresa: R${total_salarios_liquidos:.2f}")
print(f"e) % de funcionárias com mais de 3 dependentes: {percent_fem_dependentes_maior3:.2f}%")
