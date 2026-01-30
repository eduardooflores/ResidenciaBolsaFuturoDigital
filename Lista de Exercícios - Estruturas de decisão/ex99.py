pratos = {
    'vegetariano': 180,
    'peixe': 230,
    'frango': 250,
    'carne': 350,
}

sobremesas = {
    'abacaxi': 75,
    'sorvete diet': 110,
    'mousse diet': 170,
    'mousse chocolate': 200,
}

bebidas = {
    'chá': 20,
    'suco de laranja': 70,
    'suco de melão': 100,
    'refrigerante diet': 65,
}

total_calorias = 0

prato = input("Informe o prato: ").lower()
sobremesa = input("Informe a sobremesa: ").lower()
suco = input("Informe a bebida: ").lower()

if prato in pratos:
    total_calorias += pratos[prato]
else:
    print("Prato inválido. Escolha entre:", ", ".join(pratos.keys()))

if sobremesa in sobremesas:
    total_calorias += sobremesas[sobremesa]
else:
    print("Sobremesa inválida. Escolha entre:", ", ".join(sobremesas.keys()))

if suco in bebidas:
    total_calorias += bebidas[suco]
else:
    print("Bebida inválida. Escolha entre:", ", ".join(bebidas.keys()))

print(f"O total de calorias da refeição é: {total_calorias}")
