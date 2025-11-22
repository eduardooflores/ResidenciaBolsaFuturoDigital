#  Questão 63. Considerando uma eleição com 2 candidatos, elabore um algoritmo que lê o número
# total de eleitores, o número de votos do 1o candidato e o número de votos do 2o candidato. O
# algoritmo deverá apresentar o percentual de votos de cada um dos candidatos e o percentual de
# votos nulos.

# ENTRADA
numero_total_eleitores = int(input("Digite o número total de eleitores: "))
votos_primeiro_candidato = int(input("Digite a quantidade de votos do primeiro candidato: "))
votos_segundo_candidato = int(input("Digite a quantidade de votos do segundo candidato: "))
votos_nulos = int(input("Digite a quantidade de votos nulos: "))

# PROCESSAMENTO
percentual_primeiro_candidato = (votos_primeiro_candidato / numero_total_eleitores) * 100
percentual_segundo_candidato = (votos_segundo_candidato / numero_total_eleitores) * 100
percentual_votos_nulos = (votos_nulos / numero_total_eleitores) * 100

# SAÍDA
print(f"Percentual do 1º candidato: {percentual_primeiro_candidato:.2f}%")
print(f"Percentual do 2º candidato: {percentual_segundo_candidato:.2f}%")
print(f"Percentual de votos nulos: {percentual_votos_nulos:.2f}%")
