litros_vendidos = float(input("Digite o total de litros vendidos: "))
tipo_combustivel = input("Insira o tipo de combustível: (1 - álcool ou 2 - gasolina) ")
preco_combustivel = float(input("Insira o preço do combustível: R$"))

if tipo_combustivel == '1' or tipo_combustivel == '2':
    valor_bruto = litros_vendidos * preco_combustivel

    if tipo_combustivel == '1':
        if litros_vendidos <= 20:
            desconto = 0.03
        else:
            desconto = 0.05

    elif tipo_combustivel == '2':
        if litros_vendidos <= 15:
            desconto = 0.035
        else:
            desconto = 0.06

    valor_desconto = valor_bruto * desconto
    valor_final = valor_bruto - valor_desconto

    print(f"\nNúmero de litros: {litros_vendidos:.2f}")
    print(f"Preço por litro: R${preco_combustivel:.2f}")
    print(f"Valor a ser pago: R${valor_final:.2f}")

else:
    print("Insira um tipo de combustível válido!")
