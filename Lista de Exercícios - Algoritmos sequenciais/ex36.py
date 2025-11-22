# Que stão 36. Elabore um algoritmo que lê o raio de um círculo e mostre como saída o perímetro e
# a área.

# ENTRADA
raio_circulo = 20
PI = 3.14

# PROCESSAMENTO
perimetro = 2 * PI * raio_circulo
area = PI * (raio_circulo ** 2)

# SAÍDA
print(f"O perímetro do circulo é de: {perimetro:.2f}")
print(f"A área do circulo é de: {area:.2f}")
