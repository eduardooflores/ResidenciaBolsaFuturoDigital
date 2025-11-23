flag = True

total_salario = 0
total_habitantes = 0

maior_idade = 0
menor_idade = None
maior_salario = 0
maior_salario_feminino = 0
menor_idade_masculino = None

feminino_salario_maior_500 = 0
masculino_15_50 = 0
idade_18_65_salario_maior_1000 = 0

while flag:
    try:
        idade = int(input("Digite a idade: "))
        sexo = int(input("Digite o sexo (1-Feminino, 2-Masculino): "))
        salario = float(input("Digite o salário: "))

        total_salario += salario
        total_habitantes += 1

        if idade > maior_idade:
            maior_idade = idade

        if menor_idade is None or idade < menor_idade:
            menor_idade = idade

        if salario > maior_salario:
            maior_salario = salario

        if sexo == 1 and salario > maior_salario_feminino:
            maior_salario_feminino = salario

        if sexo == 2:
            if menor_idade_masculino is None or idade < menor_idade_masculino:
                menor_idade_masculino = idade

        if sexo == 1 and salario > 500:
            feminino_salario_maior_500 += 1

        if sexo == 2 and 15 <= idade <= 50:
            masculino_15_50 += 1

        if 18 <= idade <= 65 and salario > 1000:
            idade_18_65_salario_maior_1000 += 1

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
        print("ERRO! Digite valores numéricos válidos.")

media_salario = total_salario / total_habitantes if total_habitantes > 0 else 0

print("\n--- RESULTADOS DA PESQUISA ---")
print(f"a) Média de salário dos habitantes: R${media_salario:.2f}")
print(f"b) Maior idade: {maior_idade}")
print(f"c) Menor idade: {menor_idade}")
print(f"d) Maior salário: R${maior_salario:.2f}")
print(f"e) Maior salário das mulheres: R${maior_salario_feminino:.2f}")
print(f"f) Menor idade dos homens: {menor_idade_masculino}")
print(f"g) Mulheres com salário > R$500: {feminino_salario_maior_500}")
print(f"h) Homens com idade entre 15 e 50 anos: {masculino_15_50}")
print(f"i) Pessoas entre 18 e 65 anos com salário > R$1000: {idade_18_65_salario_maior_1000}")
