for i in range(20):
    try:
        nome = input(f"Digite o nome da pessoa {i+1}: ").strip()

        while True:
            try:
                idade = int(input(f"Digite a idade da pessoa {i+1}: "))
                if idade < 0:
                    print("Idade não pode ser negativa. Tente novamente.")
                    continue
                break
            except ValueError:
                print("Entrada inválida! Digite apenas números para a idade.")

        while True:
            sexo = input(f"Digite o sexo da pessoa {i+1} (M/F): ").strip().upper()
            if sexo in ["M", "F"]:
                break
            else:
                print("Entrada inválida! Digite apenas 'M' para masculino ou 'F' para feminino.")

        if sexo == "M" and idade > 21:
            print(f"Nome: {nome}")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")