# Questão 41. Elabora um algoritmo onde o usuário informa o tamanho de um quadrado e o
# resultado é mostrar a área e o perímetro do quadrado (Perímetro; 4 * L; área = L**2 ).

# ENTRADA
tamanho_quadrado = float(input("Digite o tamanho do quadrado: "))

# PROCESSAMENTO
area = 4 * tamanho_quadrado
perimetro = tamanho_quadrado ** 2

# SAÍDA
print(f"A área do quadrado é: {area}")
print(f"O perímetro do quadrado é: {perimetro}")