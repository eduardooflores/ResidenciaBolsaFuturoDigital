produto = input("Digite o nome do produto: ")
valor_compra = float(input("Digite o valor da compra: R$ "))

if valor_compra < 10:
    lucro = 0.70
elif valor_compra < 30:
    lucro = 0.50
elif valor_compra < 50:
    lucro = 0.40
else:
    lucro = 0.30

valor_venda = valor_compra * (1 + lucro)

print(f"Produto: {produto}")
print(f"Valor da venda: R$ {valor_venda:.2f}")
