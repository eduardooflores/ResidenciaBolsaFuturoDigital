PRECO_ALCOOL = 1.90
DESCONTO_ALCOOL_20L = 0.03
DESCONTO_ALCOOL_ACIMA_20L = 0.05

PRECO_GASOLINA = 2.50
DESCONTO_GASOLINA_20L = 0.04
DESCONTO_GASOLINA_ACIMA_20L = 0.06

# ENTRADA
litros_vendidos = float(input("Digite a quantidade de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A - álcool, G - gasolina): ").upper()

# PROCESSAMENTO
if tipo_combustivel == 'A':
    valor_total = litros_vendidos * PRECO_ALCOOL
    if litros_vendidos <= 20:
        valor_total_desconto = valor_total * (1 - DESCONTO_ALCOOL_20L)
        print(f"O valor total a pagar é de: R${valor_total_desconto:.2f}")
    elif litros_vendidos > 20:
        valor_total_desconto = valor_total * (1 - DESCONTO_ALCOOL_ACIMA_20L)
        print(f"O valor total a pagar é de: R${valor_total_desconto:.2f}")
elif tipo_combustivel == 'G':
    valor_total = litros_vendidos * PRECO_GASOLINA
    if litros_vendidos <= 20:
        valor_total_desconto = valor_total * (1 - DESCONTO_GASOLINA_20L)
        print(f"O valor total a pagar é de: R${valor_total_desconto:.2f}")
    elif litros_vendidos > 20:
        valor_total_desconto = valor_total * (1 - DESCONTO_GASOLINA_ACIMA_20L)
        print(f"O valor total a pagar é de: R${valor_total_desconto:.2f}")