quantidade_kg_morangos = float(input("Digite a quantidade de morangos (Kg): "))
quantidade_kg_macas = float(input("Digite a quantidade de maçãs (Kg): "))

total_kg_frutas = quantidade_kg_morangos + quantidade_kg_macas
valor_morangos = 0
valor_macas = 0

if quantidade_kg_morangos <= 5:
    valor_morangos = quantidade_kg_morangos * 5
else:
    valor_morangos = quantidade_kg_morangos * 4

if quantidade_kg_macas <= 5:
    valor_macas = quantidade_kg_macas * 3
else:
    valor_macas = quantidade_kg_macas * 2

valor_total = valor_morangos + valor_macas

if total_kg_frutas > 8 or valor_total > 35:
    valor_total *= 0.8  # Aplica 20% de desconto

print(f"Valor morangos: R$ {valor_morangos:.2f}")
print(f"Valor maçãs: R$ {valor_macas:.2f}")
print(f"TOTAL: R$ {valor_total:.2f}")
