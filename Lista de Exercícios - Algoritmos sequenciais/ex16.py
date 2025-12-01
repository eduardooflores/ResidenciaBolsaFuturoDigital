tamanho_arquivo = float(input("Digite o tamanho do arquivi para download (em MB): "))
velocidade_internet_Mbps = float(input("Digite a velocidade da sua internet: "))

velocidade_internet_bytes = velocidade_internet_Mbps / 8

tempo_download = velocidade_internet_bytes / tamanho_arquivo

print(f"O tempo médio para o download de um arquivo de {tamanho_arquivo}MB é de: {tempo_download}")