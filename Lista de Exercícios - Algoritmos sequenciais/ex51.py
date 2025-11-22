#  Questão 51
# Faça um algoritmo que leia a idade de uma pessoa expressa em dias
# e mostre-a expressa em anos, meses e dias.

# ENTRADA
idade_dias = int(input("Digite sua idade em dias: "))

# PROCESSAMENTO
anos = idade_dias // 365               # cada ano tem 365 dias
resto = idade_dias % 365               # dias que sobraram após contar os anos
meses = resto // 30                    # cada mês tem 30 dias (aproximação)
dias = resto % 30                      # o que sobrar são os dias

# SAÍDA
print(f"Sua idade é: {anos} anos, {meses} meses e {dias} dias.")
