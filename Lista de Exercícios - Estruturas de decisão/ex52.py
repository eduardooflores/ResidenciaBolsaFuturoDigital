VALOR_MACAS = 0.80
VALOR_MACAS_DESCONTO = 0.50

quantidade_macas = int(input("Insira a quantidade de maçãs compradas: "))

if quantidade_macas > 12:
    total = quantidade_macas * VALOR_MACAS_DESCONTO
else:
    total = quantidade_macas * VALOR_MACAS

print(f"O valor total para {quantidade_macas} maçã(s) comprada(s) é de: R${total:.2f}")