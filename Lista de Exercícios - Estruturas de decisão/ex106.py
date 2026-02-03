x = float(input("Digite um valor: "))
numerador = 8
denominador = 2 - x

if denominador == 0:
    print("Erro: divisão por zero")
else:
    resultado = numerador / denominador

    if resultado < 0:
        print("Erro: raiz de número negativo")
    else:
        fx = resultado ** 0.5
        print("f(x) =", fx)