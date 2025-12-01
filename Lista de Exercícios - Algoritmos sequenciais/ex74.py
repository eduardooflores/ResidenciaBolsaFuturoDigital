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