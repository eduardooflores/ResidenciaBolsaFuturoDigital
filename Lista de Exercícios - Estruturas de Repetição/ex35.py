valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

if valor2 <= valor1:
    print("O segundo valor deve ser maior que o primeiro.")
else:
    print(f"Valores entre {valor1} e {valor2}:")
    for i in range(valor1 + 1, valor2):
        print(i)
