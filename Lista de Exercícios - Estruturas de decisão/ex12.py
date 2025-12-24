numero = int(input("Digite um número: "))

if numero > 0:
    quadrada = numero ** 0.5
    print(f"A raiz quadrada do número {numero} é {quadrada}")
elif numero < 0:
    quadrado = numero * numero
    print(f"O quadrado do número {numero} é {quadrado}")
else:
    print("O número é zero")