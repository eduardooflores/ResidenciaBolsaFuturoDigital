# Q uestão 46. Em época de pouco investimento e poucas vendas, os comerciantes estão buscando
# aumentar a venda de seus produtos oferencendo descontos. Faça um algoritmo que possa receber
# o valor de um produto e que mostre: o valor do produto, o novo valor do produto considerando um
# desconto de 9% e qual foi o desconto dado. Por exemplo, o valor do produto é R$10,00, com o
# desconto de 9% o valor do produto fica R$ 9,10, e o desconto foi de R$0,90.

# ENTRADA
valor_produto = float(input("Digite o valor do produto: "))
DESCONTO = 0.09

# PROCESSAMENTO
valor_desconto = valor_produto * DESCONTO
valor_total = valor_produto - valor_desconto

# SAÍDA
print(f"O valor do produto é R${valor_produto:.2f}, com o desconto de 9% o valor do produto fica R${valor_total:.2f}, e o desconto foi de R${valor_desconto:.2f}")