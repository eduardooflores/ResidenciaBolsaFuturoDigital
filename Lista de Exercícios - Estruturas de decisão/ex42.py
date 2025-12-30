n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

maior_numero = None
menor_numero = None

if n1 > n2:
    maior_numero = n1
    menor_numero = n2
elif n2 > n1:
    maior_numero = n2
    menor_numero = n1
else:
    print("Os números são iguais")
    maior_numero = 0
    menor_numero = 0

quadrado = menor_numero * menor_numero
raiz_quadrada = maior_numero ** 0.5

if maior_numero != 0 and menor_numero != 0:
    print(f"O quadrado do menor número é: {quadrado}")
    print(f"A raiz quadrada do menor número é: {raiz_quadrada:.2f}")
else:
    pass