numero = int(input("Digite um número inteiro com 3 dígitos: "))

centena = numero // 100  # Divide por 100 para "remover" as dezenas e unidades

if centena % 2 == 0:
    print("O algarismo da casa das centenas é par.")
else:
    print("O algarismo da casa das centenas é ímpar.")
