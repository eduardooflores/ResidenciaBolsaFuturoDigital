# Q uestão 58. A equipe Ferrari deseja calcular o número mínimo de litros que deverá colocar no
# tanque de seu carro para que ele possa percorrer um determinado número de voltas até o primeiro
# reabastecimento. Escreva um algoritmo que leia o comprimento da pista (em metros), o número
# total de voltas a serem percorridas no grande prêmio, o número de reabastecimentos desejados, e
# o consumo de combustível do carro (em Km/l). Calcular e escrever o número mínimo de litros
# necessários para percorrer até o primeiro reabastecimento. OBS: Considere que o número de voltas
# entre os reabastecimentos é o mesmo.
# [Exemplo de dados de entrada]
# 4000 (comprimento da pista em metros)
# 70 (quantidade de voltas)
# 3 (quantidade de reabastecimentos)
# 3.5 (consumo em Km/l)
# [Saída para os dados de entrada acima]
# 20 (quantidade mínima de litros)

# ENTRADA
comprimento_pista = float(input("Digite o comprimento da pista em metros: "))
numero_voltas = int(input("Digite o número de voltas do grande prêmio: "))
numero_reabastecimentos = int(input("Digite o número de reabastecimentos desejados: "))
consumo = float(input("Didigie o consumo de combustível do carro em (Km/l): "))

# PROCESSAMENTO
comprimento_km = comprimento_pista / 1000 # Converte o comprimento para quilômetros
voltas_por_trecho = numero_voltas / (numero_reabastecimentos + 1)
distancia_primeiro_reabastecimento = voltas_por_trecho * comprimento_km
litros_necessarios = distancia_primeiro_reabastecimento / consumo

# SAÍDA
print(f"{litros_necessarios:.0f} Litros (quantidade mínima para o primeiro reabasteciento)")