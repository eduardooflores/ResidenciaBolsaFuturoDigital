# Questão 42. Calcule e mostre a área de um triângulo e mostre a área de um losango.

# ENTRADA
base_triangulo = float(input("Digite o a base do triangulo: "))
altura_triangulo = float(input("Digite a algura do triangulo: "))

diagonal_maior = float(input("Digite a diagonal maior: "))
diagonal_menor = float(input("Digite a diagonal menor: "))

# PROCESSAMENO
area_triangulo = (base_triangulo * altura_triangulo) / 2
area_losango = (diagonal_maior * diagonal_menor) / 2

# SAÍDA
print(f"A área do triangulo é: {area_triangulo}")
print(f"A área do losango é: {area_losango}")