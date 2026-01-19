print("-------MENU-------")
print("1 - Quadrado (lado²)")
print("2 - Retângulo (comprimento * largura)")
print("3 - Círculo (3,14 * raio²)")
print("4 - Trapézio ((base maior + base menor) * altura / 2)")

opcao = int(input("Digite a opção de cálculo desejada: "))

if opcao == 1:
    print("QUADRADO")
    lado = float(input("Digite o lado do quadrado: "))
    area_quadrado = lado * lado
    print(f"A área de um quadrado com lado {lado} é: {area_quadrado}")
elif opcao == 2:
    print("RETÂNGULO")
    comprimento = float(input("Digite o comprimento do Retângulo: "))
    largura = float(input("Digite a largura do Retângulo: "))
    area_retangulo = comprimento * largura
    print(f"A área do retângulo de comprimento {comprimento} e largura {largura} é: {area_retangulo}")
elif opcao == 3:
    print("CÍRCULO")
    raio = float(input("Digite o raio do Círculo: "))
    area_circulo = 3.14 * (raio ** 2)
    print(f"A área do círculo de raio {raio} é: {area_circulo}")
elif opcao == 4:
    print("TRAPÉZIO")
    base_maior = float(input("Digite a base maior do Trapézio: "))
    base_menor = float(input("Digite a base menor do Trapézio: "))
    altura = float(input("Digite a altura do Trapézio: "))
    area_trapezio = (base_maior + base_menor) * altura / 2
    print(f"A área do trapézio é: {area_trapezio}")
else:
    print("Você deve digitar uma opção do menu!")
