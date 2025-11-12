# Questão 1. Faça um algoritmo que lê um número e verificar se ele é par ou é ímpar.

# ENTRADA
numero = int(input("Digite um número inteiro para verificar se é par ou ímpar: "))

# PROCESSAMENTO
if numero % 2 == 0:
    print("O número é PAR")
else:
    print("O número é ÍMPAR")