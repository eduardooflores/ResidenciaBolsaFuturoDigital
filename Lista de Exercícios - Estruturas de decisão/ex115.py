ano_automovel = int(input("Digite o ano ano do automóvel: "))
peso_automovel = float(input("Digite o peso do automóvel: "))

if ano_automovel <= 1970:
    if peso_automovel < 1200:
        classe = 1
        taxa_registro = 16.50
    elif peso_automovel <= 1700:
        classe = 2
        taxa_registro = 22.50
    else:
        classe = 3
        taxa_registro = 46.50

elif ano_automovel<= 1979:
    if peso_automovel < 1200:
        classe = 4
        taxa_registro = 27.00
    elif peso_automovel <= 1700:
        classe = 5
        taxa_registro = 30.50
    else:
        classe = 6
        taxa_registro = 52.50
else:
    if peso_automovel < 3600:
        classe = 7
        taxa_registro = 19.50
    else:
        classe = 8
        taxa_registro = 52.50

print(f"A classe do seu carro é {classe} e a taxa de registro é: R${taxa_registro:.2f}")