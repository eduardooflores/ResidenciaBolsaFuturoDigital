mensalidades = {
    1: 300,  # pré-escola
    2: 400,  # 1º ciclo fundamental
    3: 500,  # 2º ciclo fundamental
    4: 600   # ensino médio
}

total_escola = 0
flag = True

while flag:
    try:
        num_filhos = int(input("\nDigite o número de filhos (0 para encerrar): "))
        if num_filhos == 0:
            flag = False
            continue

        valor_familia = 0

        for i in range(1, num_filhos + 1):
            print(f"\nFilho {i}:")
            print("Escolaridade: 1-Pré-escola | 2-1º ciclo | 3-2º ciclo | 4-Ensino Médio")
            nivel = int(input("Digite o nível escolar: "))

            if nivel in mensalidades:
                valor_base = mensalidades[nivel]
            else:
                print("Nível inválido! Considerando pré-escola.")
                valor_base = mensalidades[1]

            desconto = (i - 1) * 0.10  # 0% para o 1º, 10% para o 2º, 20% para o 3º...
            if desconto > 0.90:  # limite de 90% de desconto
                desconto = 0.90

            valor_final = valor_base * (1 - desconto)
            valor_familia += valor_final

            print(f"Mensalidade base: R${valor_base:.2f} | Desconto: {desconto*100:.0f}% | Valor final: R${valor_final:.2f}")

        total_escola += valor_familia
        print(f"\nValor total da família: R${valor_familia:.2f}")

    except ValueError:
        print("ERRO! Digite apenas números válidos.")

print("\n--- RESULTADO FINAL ---")
print(f"Total arrecadado pela escola: R${total_escola:.2f}")
