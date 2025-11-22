# Questão 16. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
# velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download
# do arquivo usando este link (em minutos).

tamanho_arquivo = float(input("Digite o tamanho do arquivi para download (em MB): "))
velocidade_internet_Mbps = float(input("Digite a velocidade da sua internet: "))

velocidade_internet_bytes = velocidade_internet_Mbps / 8

tempo_download = velocidade_internet_bytes / tamanho_arquivo

print(f"O tempo médio para o download de um arquivo de {tamanho_arquivo}MB é de: {tempo_download}")