# Q uestão 38. Elabore um algoritmo que lê um número e imprime a raiz quadrada do número.

# ENTRADA
numero = int(input("Digite um número inteiro: "))

# PROCESSAMENTO
raiz_quadrada = pow(numero, 0.5)
raiz_quadrada_outra_forma = numero ** 0.5

# SAÍDA
print(f"A raiz quadrada do número {numero} é de: {raiz_quadrada}")