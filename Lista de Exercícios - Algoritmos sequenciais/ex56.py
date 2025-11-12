# Questão 56. Escreva um algoritmo para ler o número de eleitores de um município, o número de
# votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação
# ao total de eleitores.
# [Exemplo de dados de entrada]
# 200 (quantidade de eleitores)
# 10 (quantidade de votos brancos)
# 20 (quantidade de votos nulos)
# 160 (quantidade de votos válidos)
# [Saída para os dados de entrada acima]
# 5 (percentual de votos brancos)
# 10 (percentual de votos nulos)
# 80 (percentual de votos válidos)

# ENTRADA
eleitores = int(input("Digite a quantidade de eleitores: "))
votos_brancos = int(input("Digite a quantidade de votos brancos: "))
votos_nulos = int(input("Digite a quantidade de votos nulos: "))
votos_validos = int(input("Digite a quantidade de votos válidos: "))

# PROCESSAMENTO
percentual_votos_brancos = (votos_brancos / eleitores) * 100
percentual_votos_nulos = (votos_nulos / eleitores) * 100
percentual_votos_validos = (votos_validos / eleitores) * 100

# SAÍDA
print(f"{percentual_votos_brancos:.2f} (percentual de votos brancos)")
print(f"{percentual_votos_nulos:.2f} (percentual de votos nulos)")
print(f"{percentual_votos_validos:.2f} (percentual de votos válidos)")