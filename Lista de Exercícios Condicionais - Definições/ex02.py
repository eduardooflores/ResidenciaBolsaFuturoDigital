# ENTRADA
combustivel = input("Digite o tipo de conbustível: A - Álcool , G - Gasolina: ").upper()
litros = float(input("Digite a quantidade de litros vendidos: "))
PRECO_GASOLINA = 6.10
PRECO_ALCOOL = 5.75

# PROCESSAMENTO
if combustivel == "G" and litros <= 20 and litros > 0:
    desconto = PRECO_GASOLINA * 0.035
    valor_total = litros * (PRECO_GASOLINA - desconto)
    print(f"O valor total a pagar: R${valor_total:.2f}")

elif combustivel == "G" and litros > 20 and litros > 0:
    desconto = PRECO_GASOLINA * 0.10
    valor_total = litros * (PRECO_GASOLINA - desconto)
    print(f"O valor total a pagar: R${valor_total:.2f}")

elif combustivel == "A" and litros <= 20 and litros > 0:
    desconto = PRECO_ALCOOL * 0.055
    valor_total = litros * (PRECO_ALCOOL - desconto)
    print(f"O valor total a pagar: R${valor_total:.2f}")

elif combustivel == "A" and litros > 20 and litros > 0:
    desconto = PRECO_ALCOOL * 0.08
    valor_total = litros * (PRECO_ALCOOL - desconto)
    print(f"O valor total a pagar: R${valor_total:.2f}")

elif combustivel != "G" and combustivel != "A" and litros <= 0:
    print("CÓDIGO INVÁLIDO")
    print("QUANTIDADE INVÁLIDA")

elif combustivel != "G" and combustivel != "A":
    print("CÓDIGO INVÁLIDO")

else:
    print("QUANTIDADE INVÁLIDA")