flag = True

total_salario = 0
total_filhos = 0
maior_salario = 0
pessoas = 0
salarios_ate_200 = 0

while flag:
    try:
        salario = float(input("Digite o salário da família: "))
        filhos = int(input("Digite o número de filhos da família: "))

        total_salario += salario
        total_filhos += filhos
        pessoas += 1

        if salario > maior_salario:
            maior_salario = salario

        if salario <= 200:
            salarios_ate_200 += 1

        # pergunta se deseja continuar
        flag_op = True
        while flag_op:
            try:
                op = int(input("Deseja continuar o cadastro? (1.Sim 2.Não): "))
                if op == 1:
                    flag_op = False
                elif op == 2:
                    flag_op = False
                    flag = False
                else:
                    print("Digite 1 para continuar ou 2 para sair.")
            except ValueError:
                print("ERRO! Digite apenas números (1 ou 2).")

    except ValueError:
        print("ERRO! Dados inválidos. Digite corretamente.")

media_salario = total_salario / pessoas if pessoas > 0 else 0
media_filhos = total_filhos / pessoas if pessoas > 0 else 0
percentual_ate_200 = (salarios_ate_200 / pessoas * 100) if pessoas > 0 else 0

# resultados
print("\n--- RESULTADOS DA PESQUISA ---")
print(f"Média do salário da população: R${media_salario:.2f}")
print(f"Média do número de filhos: {media_filhos:.2f}")
print(f"Maior salário: R${maior_salario:.2f}")
print(f"Percentual de pessoas com salário até R$200,00: {percentual_ate_200:.2f}%")
