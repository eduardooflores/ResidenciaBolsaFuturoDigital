# Q uestão 57. Um motorista de taxi deseja calcular o rendimento de seu carro na praça. Sabendose que o preço
# do combustível é de R$ 2,50, escreva um algoritmo para ler: a marcação do odômetro
# (Km) no início do dia, a marcação (Km) no final do dia, o número de litros de combustível gasto e o
# valor total (R$) recebido dos passageiros. Calcular e escrever: a média do consumo em Km/L e o
# lucro (líquido) do dia.
# [Exemplo de dados de entrada]
# 1500 (marcação no início do dia)
# 1700 (marcação no fim do dia)
# 20 (quantidade de litros de combustível)
# 80 (valor recebido)
# [Saída para os dados de entrada acima]
# 10 (média de consumo)
# 30 (lucro)

# ENTRADA
COMBUSTIVEL = 2.50
odometro_inicio = float(input("Digite a marcação do odômetro (km) do início do dia: "))
odometro_fim = float(input("Digite a marcação do odõmetro (km) do fim do dia: "))
combustivel_gastro = float(input("Digite o número de litros de combustível gasto: "))
valor_recebido = float(input("Digite o valor total recebido no dia: "))

# PROCESSAMENTO
distancia_km = odometro_fim - odometro_inicio
media_consumo = distancia_km / combustivel_gastro
valor_total_gasto = combustivel_gastro * COMBUSTIVEL
valor_total_liquido = valor_recebido - valor_total_gasto

# SAÍDA
print(f"{media_consumo} (média consumo)")
print(f"{valor_total_liquido} (lucro)")