# Q uestão 44. O restaurante a quilo Bem-Bao cobra R$12,00 por cada quilo de refeição. Escreva um
# algoritmo que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar.
# Assuma que a balança ja desconte o peso do prato.

# ENTRADA
VALOR_KILO = 12
peso_prato_kilos = float(input("Digite o peso do prato em kilos: "))

# PROCESSAMENTO
valor_total = peso_prato_kilos * VALOR_KILO

# SAÍDA
print(f"O valor total a pagar é de: R$ {valor_total:.2f}")