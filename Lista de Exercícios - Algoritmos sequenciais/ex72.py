# ENTRADA
DESCONTO = 0.25

numero_apartamentos = int(input("Digite o número de apartamentos do hotel: "))
valor_diaria_apartamento = float(input("Digite o valor da diária dos apartamentos: "))

# PROCESSAMENTO
# Valor promocional da diária (com desconto)
valor_promocional_diaria = valor_diaria_apartamento * (1 - DESCONTO)

# Valor total com ocupação de 100%
valor_total_100 = valor_promocional_diaria * numero_apartamentos

# Valor total com ocupação de 70%
valor_total_70 = valor_total_100 * 0.7

# Valor que o hotel deixará de arrecadar por causa do desconto (ocupação 100%)
valor_perda = (valor_diaria_apartamento - valor_promocional_diaria) * numero_apartamentos

# SAÍDA
print(f"Valor promocional da diária: R$ {valor_promocional_diaria:.2f}")
print(f"Valor total com 100% de ocupação: R$ {valor_total_100:.2f}")
print(f"Valor total com 70% de ocupação: R$ {valor_total_70:.2f}")
print(f"Valor que o hotel deixará de arrecadar devido à promoção (100% ocupação): R$ {valor_perda:.2f}")