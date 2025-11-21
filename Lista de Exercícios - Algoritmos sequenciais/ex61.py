# Questão 61. Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer do
# plano, P(x1, y2) e Q(x2, y2), mostre na tela a distância entre eles. A fórmula para efetuar tal cálculo
# é d = raizQuatrada((x2 − x1) 2 − (y2 − y1) 2)

# ENTRADA
x1 = float(input("Digite o valor de x1: "))
y1 = float(input("Digite o valor de y1: "))
x2 = float(input("Digite o valor de x2: "))
y2 = float(input("Digite o valor de y2: "))

# PROCESSAMENTO
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# SAÍDA
print(f"A distância entre os pontos P({x1}, {y1}) e Q({x2}, {y2}) é {distancia:.2f}")