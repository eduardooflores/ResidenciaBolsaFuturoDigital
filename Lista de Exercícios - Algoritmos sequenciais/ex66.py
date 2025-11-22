# Q uestão 66. Faça um algoritmo que lê o público total de um jogo de futebol e fornece a renda do
# jogo, sabendo que havia 4 tipos de ingressos assim distribuídos: popular - 10% a R$1,00, geral - 50%
# a R$5,00, arquibancada - 30% a R$10,00 e cadeiras - 10% a R$20,00.

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