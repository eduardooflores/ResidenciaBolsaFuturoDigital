# Questão 3. Faça um algoritmo que leia um número e mostrar se ele é positivo, negativo ou igual
# a zero.

# ENTRADA
numero = int(input("Digite um número: "))

# PROCESSAMENTO
if numero > 0:
    print(f"O número {numero} é positivo!")
elif numero < 0:
    print(f"O número é negativo")
else:
    print("O número é igual a zero")
