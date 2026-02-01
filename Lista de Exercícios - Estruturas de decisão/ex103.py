salario = float(input("Insira o salário: "))

if salario <= 600:
    print("Isento de INSS")
elif salario <= 1200:
    valor_inss = salario * 0.2
    print(f"O valor descontado do INSS é: R${valor_inss:.2f}")
elif salario <= 2000:
    valor_inss = salario * 0.25
    print(f"O valor descontado do INSS é: R${valor_inss:.2f}")
else:
    valor_inss = salario * 0.30
    print(f"O valor descontado do INSS é: R${valor_inss:.2f}")
