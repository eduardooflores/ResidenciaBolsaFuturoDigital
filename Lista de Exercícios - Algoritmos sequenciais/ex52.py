# ENTRADA
SALARIO = 1200
MULTA = 0.02

c1 = 200
c2 = 120

# PROCESSAMENTO
c1_multa = c1 * MULTA
c2_multa = c2 * MULTA

c1_total = c1 + c1_multa
c2_total = c2 + c2_multa

salario_liquido = SALARIO - (c1_total + c2_total)

# SAÍDA
print(f"O salário total é de: R${salario_liquido:.2f}")