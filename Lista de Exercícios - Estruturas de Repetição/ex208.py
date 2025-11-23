classes = {
    1: ("Excelente", 1.00),   # +100%
    2: ("Bom", 0.80),         # +80%
    3: ("Médio", 0.50),       # +50%
    4: ("Regular", 0.30),     # +30%
    5: ("Precisa treinar mais", 0.10),  # +10%
    6: ("Te cuida", 0.05),    # +5%
    7: ("Tsktsk nada", 0.00)  # sem adicional
}

flag = True
while flag:
    try:
        salario = float(input("\nDigite o salário do jogador: R$"))
        codigo = int(input("Digite o código da classe (1 a 7, outro número encerra): "))

        if codigo not in classes:
            print("\nCódigo fora do intervalo. Encerrando programa...")
            flag = False
            continue

        nivel, adicional = classes[codigo]
        salario_final = salario + (salario * adicional)

        print("\n--- RESULTADO ---")
        print(f"Classe: {nivel}")
        print(f"Salário base: R${salario:.2f}")
        print(f"Adicional: {adicional*100:.0f}%")
        print(f"Salário final: R${salario_final:.2f}")

    except ValueError:
        print("ERRO! Digite valores numéricos válidos.")
