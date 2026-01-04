tempo_de_servico = int(input("Informe quantos anos o trabalhador está na empresa: "))
salario = float(input("Informe o salário do trabalhador: "))

if tempo_de_servico >= 5:
    bonus = salario * 0.20
    total = salario + bonus
    print(f"O valor total do bônus é de: R${total:.2f}")
else:
    bonus = salario * 0.10
    total = salario + bonus
    print(f"O valor total do bônus é de: R${total:.2f}")