# Q uestão 72. Um hotel deseja fazer uma promoção especial de final de semana, concedendo um
# desconto de 25% na diária. O usuário informará o número de apartamentos do hotel e o valor da
# diária por apartamento por final de semana. Elabore um algoritmo para calcular:
# • Valor promocional da diária;
# • Valor total a ser arrecadado caso a ocupação total (100%) seja atingida;
# • Valor total a ser arrecadado caso a ocupação seja de 70%.
# • Valor que o hotel deixará de arrecadar em virtude da promoção, caso a ocupação atinja 100%.

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