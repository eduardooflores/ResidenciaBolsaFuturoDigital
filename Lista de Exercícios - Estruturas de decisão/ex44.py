numero = int(input("Digite um número: "))

if numero % 10 == 0:
    print("Número divisível por 10")
elif numero % 5 == 0:
    print("Número divisível por 5")
elif numero % 2 == 0:
    print("Número divisível por 2")
else:
    print(f"O número {numero} não é divisível por 10, 5 ou 2")