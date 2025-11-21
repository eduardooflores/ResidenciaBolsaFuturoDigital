# Questão 68. Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas
# vendas oferecendo desconto. Faça um algoritmo que possa entrar com o valor de um produto e
# imprima o novo valor tendo em vista que o desconto foi de 9%.

# ENTRADA
DESCONTO = 0.09

valor_produto = float(input("Digite o valor do produto: "))

# PROCESSAMENTO
valor_desconto = valor_produto * (1 - DESCONTO)

# SAÍDA
print(f"O valor total do produto com um desconto de 9% é de: R${valor_desconto:.2f}")