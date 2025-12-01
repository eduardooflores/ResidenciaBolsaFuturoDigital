# ENTRADA
valor_produto = float(input("Digite o valor do produto: "))
DESCONTO = 0.09

# PROCESSAMENTO
valor_desconto = valor_produto * DESCONTO
valor_total = valor_produto - valor_desconto

# SAÍDA
print(f"O valor do produto é R${valor_produto:.2f}, com o desconto de 9% o valor do produto fica R${valor_total:.2f}, e o desconto foi de R${valor_desconto:.2f}")