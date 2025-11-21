# Questão 74. Faça um algoritmo que leia a quantidade de DVDs que uma locadora possui e o valor
# que ela cobra por cada aluguel, mostrando ao final as informações de acordo com as questões:
# • Sabe-se que um terço dos DVDs são alugadas por mês, mostre o faturamento anual da
# locadora;
# • Quando um cliente atrasa a entrega, é cobrada uma multa de 10% sobre o valor do aluguel.
# Sabe-se que um décimo dos DVDs alugados no mês são devolvidos com atraso, calcule o
# valor ganho com multas por mês;
# • Sabe-se ainda que 2% dos DVDs acabam estragando ao longo do ano, e um décimo do total
# é comprado para reposição, mostre a quantidade de DVDs que a locadora terá no final do
# ano.

# CONSTANTES
ATRASO = 0.10      # 10% de multa
ESTRAGADOS = 0.02  # 2% estragam
REPOSICAO = 0.10   # 10% são comprados

# ENTRADA
qntd_dvds = int(input("Informe a quantidade de DVDs disponíveis na locadora: "))
valor_aluguel = float(input("Digite o valor do aluguel dos DVDs: "))

# PROCESSAMENTO
# 1) Faturamento anual
alugados_mes = qntd_dvds / 3
faturamento_mes = alugados_mes * valor_aluguel
faturamento_ano = faturamento_mes * 12

# 2) Valor das multas
atrasados_mes = alugados_mes / 10
multa_por_dvd = valor_aluguel * ATRASO
valor_multas_mes = atrasados_mes * multa_por_dvd

# 3) Quantidade final de DVDs
estragados_ano = qntd_dvds * ESTRAGADOS
comprados_ano = qntd_dvds * REPOSICAO
qntd_dvds_final = qntd_dvds - estragados_ano + comprados_ano

# SAÍDA
print(f"\nFaturamento anual: R${faturamento_ano:.2f}")
print(f"Valor ganho com multas por mês: R${valor_multas_mes:.2f}")
print(f"Quantidade de DVDs ao final do ano: {qntd_dvds_final:.0f}")