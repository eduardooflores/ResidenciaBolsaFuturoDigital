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