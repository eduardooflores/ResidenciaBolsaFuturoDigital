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