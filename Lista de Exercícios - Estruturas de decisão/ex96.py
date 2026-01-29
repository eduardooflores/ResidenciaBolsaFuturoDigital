nome = input("Digite o nome da pessoa: ").title()
idade = int(input("Digite a idade da pessoa: "))

if idade <= 10:
    preco = 30
elif idade <= 29:
    preco = 60
elif idade <= 45:
    preco = 120
elif idade <= 59:
    preco = 150
elif idade <= 65:
    preco = 250
else:
    preco = 400

print(f"{nome} com {idade} anos. Deverá pagar: R${preco},00")