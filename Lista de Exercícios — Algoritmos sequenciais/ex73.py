# Questão 73. Um hotel com 42 apartamentos resolveu fazer promoções para os fins de semana fora
# da alta temporada, isto é, nos meses de abril, maio, junho, agosto, setembro, outubro e novembro.
# A taxa da promoção é de 22% da diária normal. A ocupação média do hotel sem promoção é de 40%.
# A expectativa é aumentar a taxa de ocupação para 70%. Supondo que as expectativas se confirmem,
# faça um algoritmo que lê o valor da diária normal, calcula o mostra as informações:
# • O valor da diária no período da promoção;
# • O valor médio arrecadado sem a promoção, durante um mês; o valor médio arrecadado com
# a promoção, durante um mês;
# • O lucro ou prejuízo mensal com a promoção.

# ENTRADA
APARTAMENTOS = 42
PROMOCAO = 0.22
OCUPACAO_MEDIA = 0.40
OCUPACAO_ESPECTATIVA = 0.70
FINAIS_DE_SEMANA = 4

valor_diaria = float(input("Digite o valor da diária: "))

# PROCESSAMENTO
valor_diaria_promocao = valor_diaria * (1 - PROMOCAO)
valor_medio_sem_promocao = valor_diaria * APARTAMENTOS * OCUPACAO_MEDIA * FINAIS_DE_SEMANA
valor_medio_com_promocao = valor_diaria_promocao * APARTAMENTOS * OCUPACAO_ESPECTATIVA * FINAIS_DE_SEMANA
lucro_ou_prejuizo = valor_medio_com_promocao - valor_medio_sem_promocao

# SAÍDA
print(f"Valor da diária durante a promoção: R$ {valor_diaria_promocao:.2f}")
print(f"Valor médio arrecadado sem a promoção: R$ {valor_medio_sem_promocao:.2f}")
print(f"Valor médio arrecadado com a promoção: R$ {valor_medio_com_promocao:.2f}")
print(f"Lucro/Prejuízo mensal com a promoção: R$ {lucro_ou_prejuizo:.2f}")
