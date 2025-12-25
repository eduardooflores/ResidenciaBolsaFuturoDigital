numero = int(input("Digite um número inteiro: "))

if numero >= 10 and numero <= 20:
    print(f"O número {numero} está no intervalor de 10 e 20")
elif numero >= 21 and numero <= 30:
    print(f"O número {numero} está no intervalor de 21 e 30")
elif numero > 90:
    print(f"O número {numero} é maior que 90")
else:
    print(f"O número {numero} está fora dos intervalos")