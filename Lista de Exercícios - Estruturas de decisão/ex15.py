# Questão 15. Faça um algoritmo que leia um número e mostre se ele é divisível por 5 OU por 9.

# ENTRADA
numero = int(input("Digite um número inteiro: "))

# PROCESSAMENTO
if numero % 5 == 0:
    print(f"O número {numero} é divisível por 5")
elif numero % 9 == 0:
    print(f"O número {numero} é divisível por 9")
else:
    print(f"O número {numero} não é divisível por 5 nem por 9")
