#  Questão 37. Elabore um algoritmo que calcula e mostra a média das notas de todos os alunos de
# Algoritmos e Lógica de Programação.

#ENTRADA
nome = input("Digite seu nome: ")
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))
nota_4 = float(input("Digite a quarta nota: "))

# PROCESSAMENTO
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

# SAÍDA
print(f"A média da nota do aluno {nome} é de: {media:.2f}")