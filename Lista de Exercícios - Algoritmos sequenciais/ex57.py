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