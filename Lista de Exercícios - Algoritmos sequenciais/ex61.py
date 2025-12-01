# ENTRADA
x1 = float(input("Digite o valor de x1: "))
y1 = float(input("Digite o valor de y1: "))
x2 = float(input("Digite o valor de x2: "))
y2 = float(input("Digite o valor de y2: "))

# PROCESSAMENTO
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# SAÍDA
print(f"A distância entre os pontos P({x1}, {y1}) e Q({x2}, {y2}) é {distancia:.2f}")