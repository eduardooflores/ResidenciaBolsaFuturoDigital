numero = int(input("Digite um número: "))

if numero % 3 == 0:
    print(f"Número {numero} é divisível por 3.")
if numero % 5 == 0:
    print(f"Número {numero} é divisível por 5.")
if numero % 7 == 0:
    print(f"Número {numero} é divisível por 7.")
if numero % 3 != 0 and numero % 5 != 0 and numero % 7 != 0:
    print(f"O número {numero} não é divisível por 3, 5 ou 7.")
