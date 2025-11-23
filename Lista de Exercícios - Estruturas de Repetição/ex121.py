flag = True

pessoas = 0
mais_90kg = 0
soma_idades = 0
maior_idade = 0
entre_15_50 = 0
menos_18 = 0
soma_peso_maior_50 = 0
cont_maior_50 = 0

while flag:
    try:
        idade = int(input("Digite a idade: "))
        peso = float(input("Digite o peso: "))

        pessoas += 1
        soma_idades += idade

        if idade > maior_idade:
            maior_idade = idade

        if peso > 90:
            mais_90kg += 1

        if 15 <= idade <= 50:
            entre_15_50 += 1

        if idade < 18:
            menos_18 += 1

        if idade > 50:
            soma_peso_maior_50 += peso
            cont_maior_50 += 1

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

media_idades = soma_idades / pessoas if pessoas > 0 else 0
media_peso_maior_50 = soma_peso_maior_50 / cont_maior_50 if cont_maior_50 > 0 else 0

print("\n--- RESULTADOS ---")
print(f"a) Pessoas com mais de 90kg: {mais_90kg}")
print(f"b) Média das idades: {media_idades:.2f}")
print(f"c) Maior idade: {maior_idade}")
print(f"d) Pessoas com idade entre 15 e 50 anos: {entre_15_50}")
print(f"e) Pessoas com menos de 18 anos: {menos_18}")
print(f"f) Média de peso das pessoas com idade > 50 anos: {media_peso_maior_50:.2f}")
