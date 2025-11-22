# Questão 18. Elabore um algoritmo que lê dois valores decimais e mostra a soma e o produto dos
# v alores.

numero_1 = float(input("Digite um número decimal: "))
numero_2 = float(input("Digite outro número decimal: "))

soma = numero_1 + numero_2
produto = numero_1 * numero_2

print(f"A soma dos número {numero_1:.2f} com {numero_2:.2f} é: {soma:.2f}")
print(f"O produto dos número {numero_1:.2f} com {numero_2:.2f} é: {produto:.2f}")