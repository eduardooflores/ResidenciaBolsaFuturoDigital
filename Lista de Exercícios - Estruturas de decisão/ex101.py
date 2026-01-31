a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Não é possível formar triângulo (lado inválido).")

elif a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Triângulo equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Não é possível formar triângulo")
