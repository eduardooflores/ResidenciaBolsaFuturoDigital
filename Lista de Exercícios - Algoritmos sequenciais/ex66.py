# ENTRADA
POPULAR = 1
GERAL = 5
ARQUIBANCADA = 10
CADEIRAS = 20

publico = int(input("Número total de público presente: "))

# PROCESSAMENTO
qtd_popular = publico * 0.10
qtd_geral = publico * 0.50
qtd_arquibancada = publico * 0.30
qtd_cadeiras = publico * 0.10

renda_popular = qtd_popular * POPULAR
renda_geral = qtd_geral * GERAL
renda_arquibancada = qtd_arquibancada * ARQUIBANCADA
renda_cadeiras = qtd_cadeiras * CADEIRAS

renda_total = renda_popular + renda_geral + renda_arquibancada + renda_cadeiras

# SAÍDA
print(f"Renda total do jogo: R$ {renda_total:,.2f}")