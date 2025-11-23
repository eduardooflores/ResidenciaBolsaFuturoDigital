total_vista = 0
total_prazo = 0

for i in range(1, 16):
    print(f"\nTransação {i}:")
    codigo = input("Digite o código (V - à vista, P - a prazo): ").upper()
    try:
        valor = float(input("Digite o valor da transação: "))
    except ValueError:
        print("ERRO! Digite apenas números.")
        valor = 0

    if codigo == "V":
        total_vista += valor
    elif codigo == "P":
        total_prazo += valor
    else:
        print("Código inválido! Use V ou P.")

total_loja = total_vista + total_prazo
primeira_prestacao = total_prazo / 3

print("\n--- RESULTADOS ---")
print(f"a) Valor total das compras à vista: R${total_vista:.2f}")
print(f"b) Valor total das compras a prazo: R${total_prazo:.2f}")
print(f"c) Valor total das compras efetuadas na loja: R${total_loja:.2f}")
print(f"d) Valor da primeira prestação das compras a prazo: R${primeira_prestacao:.2f}")
