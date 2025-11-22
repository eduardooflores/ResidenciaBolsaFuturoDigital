#  Questão 69. Efetuar o cálculo do valor de uma prestação em atraso, utilizando a fórmula:
# prestação = valor + (valor * (taxa/100)*tempo)

# Entrada
TAXA = 5

valor = float(input("Digite o valor da prestação: "))
tempo_atraso = int(input("Digite o tempo da prestação atrasada em dias: "))
# PROCESSAMENTO
prestacao = valor + (valor * (TAXA/100) * tempo_atraso)

# SAÍDA
print(f"O valor da prestação em atraso é de: R$ {prestacao:.2f}")
