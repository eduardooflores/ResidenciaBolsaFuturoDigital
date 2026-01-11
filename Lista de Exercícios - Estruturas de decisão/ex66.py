dvds = {
    'azul': 10.00,
    'rosa': 25.00,
    'verde': 35.00,
    'vermelho': 50.00
}

cor = input("Digite a cor do DVD (azul, rosa, verde, vermelho): ").strip().lower()

if cor in dvds:
    preco = dvds[cor]
    quantidade = int(input("Quantos DVDs você deseja comprar? "))
    total = preco * quantidade
    print(f"\nQuantidade de DVDs: {quantidade}")
    print(f"Preço por DVD ({cor}): R$ {preco:.2f}")
    print(f"Valor total a pagar: R$ {total:.2f}")
else:
    print("Cor inválida. Por favor, escolha entre azul, rosa, verde ou vermelho.")