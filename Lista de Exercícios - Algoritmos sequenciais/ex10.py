# Questão 10. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo. a soma do triplo do primeiro com o
# terceiro. o terceiro elevado ao cubo.

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
numero_real = float(input("Digite um número real (pode ter vírgula): "))

produto_do_dobro = (n1 * 2) * (n2 / 2)

soma_do_triplo = (n1 * 3) + (numero_real ** 3)