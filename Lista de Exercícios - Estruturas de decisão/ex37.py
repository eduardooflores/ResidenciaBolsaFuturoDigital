mesada = float(input("Insira o valor da mesada: "))
gasto_01 = float(input("Insira o valor do primeiro gasto: "))
gasto_02 = float(input("Insira o valor do segundo gasto: "))
gasto_03 = float(input("Insira o valor do terceiro gasto: "))
gasto_04 = float(input("Insira o valor do quarto gasto: "))
gasto_05 = float(input("Insira o valor do quinto gasto: "))

total_gastos = gasto_01 + gasto_02 + gasto_03 + gasto_04 + gasto_05

if total_gastos > mesada:
    print(f"Você não tem saldo suficiente para pagas as dívidas! SALDO: R${mesada:.2f} GASTOS: R${total_gastos:.2f}")
else:
    print(f"Você tem saldo o suficiente para pagar as dívidas! SALDO: R${mesada:.2f} GASTOS: R${total_gastos:.2f}")