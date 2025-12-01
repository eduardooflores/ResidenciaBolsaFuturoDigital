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
