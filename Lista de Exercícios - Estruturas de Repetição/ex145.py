cardapio = {
    101: 3.00,   # Cachorro Quente
    201: 5.00,   # Bauru simples
    202: 6.00,   # Bauru# Hambúrguer com ovo
    301: 4.00,
    302: 5.00,   # Cheeseburguer
    500: 2.00    # Refrigerante
}

total_pagar = 0

try:
    pessoas = int(input("Digite o número de pessoas que farão o pedido: "))

    for i in range(1, pessoas + 1):
        print(f"\nPessoa {i}:")
        try:
            codigo = int(input("Digite o código do item: "))
            quantidade = int(input("Digite a quantidade: "))

            if codigo in cardapio:
                valor_item = cardapio[codigo] * quantidade
                total_pagar += valor_item
                print(f"Item {codigo} adicionado. Valor: R${valor_item:.2f}")
            else:
                print("Código inválido! Item não existe no cardápio.")

        except ValueError:
            print("ERRO! Digite valores numéricos válidos.")

    print("\n--- RESULTADO FINAL ---")
    print(f"Valor total a ser pago: R${total_pagar:.2f}")

except ValueError:
    print("ERRO! Digite um número válido de pessoas.")
