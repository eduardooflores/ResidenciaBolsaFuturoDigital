cargos = {
    101: 0.10,  # Diretor
    102: 0.15,  # Gerente
    103: 0.20,  # Engenheiro
    104: 0.30,  # Técnico
    105: 0.35,  # Auxiliar
    106: 0.40   # Administrativo
}

flag = True
while flag:
    try:
        salario = float(input("\nDigite o salário do funcionário: R$"))
        codigo = int(input("Digite o código do cargo: "))

        if codigo in cargos:
            percentual = cargos[codigo]
        else:
            percentual = 0.50  # cargo não listado → 50%

        novo_salario = salario * (1 + percentual)
        diferenca = novo_salario - salario

        print("\n--- RESULTADO ---")
        print(f"Salário antigo: R${salario:.2f}")
        print(f"Novo salário: R${novo_salario:.2f}")
        print(f"Reajuste aplicado: R${diferenca:.2f} ({percentual*100:.0f}%)")

    except ValueError:
        print("ERRO! Digite valores numéricos válidos.")

    op= input("\nDeseja cadastrar outro funcionário? (S/N): ").upper()
    if op != "S":
        flag = False
