largura = float(input("Digite a largura: "))
comprimento = float(input("Digite o comprimento: "))


if largura <= 0 or comprimento <= 0:
    print("Valores inválidos! Digite números maiores que zero")
elif largura != comprimento:
    print("Retângulo")
else:
    print("Quadrado")