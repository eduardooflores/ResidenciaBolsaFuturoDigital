# Questão 203

try:
    salario_minimo = float(input("Digite o valor do salário mínimo: R$"))
    valor_hora = salario_minimo / 10

    flag = True
    while flag:
        horas_trabalhadas = int(input("\nDigite o número de horas trabalhadas (-1 para encerrar): "))
        if horas_trabalhadas == -1:
            flag = False
            continue

        dependentes = int(input("Digite o número de dependentes: "))
        horas_extras = int(input("Digite a quantidade de horas extras trabalhadas: "))

        salario_mes = horas_trabalhadas * valor_hora

        acrescimo_dependentes = dependentes * 32
        acrescimo_extras = horas_extras * (valor_hora * 1.5)

        salario_bruto = salario_mes + acrescimo_dependentes + acrescimo_extras

        if salario_bruto <= 900:
            desconto_ir = 0
        elif salario_bruto <= 1500:
            desconto_ir = salario_bruto * 0.10
        else:
            desconto_ir = salario_bruto * 0.20

        salario_liquido = salario_bruto - desconto_ir

        if salario_liquido <= 900:
            gratificacao = 100
        else:
            gratificacao = 50

        salario_final = salario_liquido + gratificacao

        print("\n--- RESULTADO ---")
        print(f"Salário bruto: R${salario_bruto:.2f}")
        print(f"Salário líquido: R${salario_liquido:.2f}")
        print(f"Gratificação: R${gratificacao:.2f}")
        print(f"Salário a receber: R${salario_final:.2f}")

except ValueError:
    print("ERRO! Digite valores numéricos válidos.")
