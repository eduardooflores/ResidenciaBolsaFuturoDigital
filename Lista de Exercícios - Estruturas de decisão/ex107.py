x = float(input("Digite um valor: "))

expressao_interna = x * x - 16

if expressao_interna < 0:
    print("Erro: raiz de número negativo")
else:
    raiz = expressao_interna ** 0.5
    parte_fracionaria = 3 / raiz
    resultado = 5 * x + parte_fracionaria
    print("f(x) =", resultado)