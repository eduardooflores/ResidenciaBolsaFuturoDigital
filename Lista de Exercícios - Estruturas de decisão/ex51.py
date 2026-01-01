numero = int(input("Insira um número: "))

if numero == 5:
    print("Número igual a 5")
elif numero == 200:
    print("Número igual a 200")
elif numero == 400:
    print("Número igual a 400")
elif numero >= 500 and numero <= 1000:
    print("O número está no intervalor de 500 a 1000")
else:
    print("O número está fora dos intervalos")