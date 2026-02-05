lanches = {
    "101": {"lanche": "cachorro-quente", "preco": 3.00},
    "201": {"lanche": "bauru simples", "preco": 5.00},
    "202": {"lanche": "bauru com ovo", "preco": 6.00},
    "301": {"lanche": "hambúrguer", "preco": 4.00},
    "302": {"lanche": "cheesburguer", "preco": 5.00},
    "500": {"lanche": "refrigerante", "preco": 2.00},
}

codigo_item = input("Insira o código do item pedido: ")
qntd_item = int(input("Insira a quantidade pedida: "))

if codigo_item in lanches:
    lanche = lanches[codigo_item]["lanche"]
    valor_lanche = lanches[codigo_item]["preco"] * qntd_item
    print(f"{qntd_item}x {lanche} = R$ {valor_lanche:.2f}")
else:
    print("Código de lanche inválido!")
