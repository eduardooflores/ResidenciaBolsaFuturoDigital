flag = True
idades = []
pesos = []
alturas = []
total_pessoas_cadastradas = 0
total_sexo_feminino = 0
total_sexo_masculino = 0
caracteristicas_verificador = 0

while flag:
    try:
        sexo = input("Digite o sexo (Masculino - M , Feminino - F): ").upper()
        if sexo not in ["M", "F"]:
            print("ERRO: O sexo deve ser M ou F")
            continue

        if sexo == "F":
            total_sexo_feminino += 1

        if sexo == "M":
            total_sexo_masculino += 1

        cor_olhos = input("Digite a cor dos olhos (azuis, verdes ou castanhos): ").upper()
        if cor_olhos not in ["AZUIS", "VERDES", "CASTANHOS"]:
            print("ERRO: Cor dos olhos inválida")
            continue

        cor_cabelos = input("Digite a cor dos cabelos (louros, castanhos ou pretos): ").upper()
        if cor_cabelos not in ["LOUROS", "CASTANHOS", "PRETOS"]:
            print("ERRO: Cor dos cabelos inválida")
            continue

        if cor_olhos == "VERDES" and cor_cabelos == "LOUROS":
            caracteristicas_verificador += 1

        idade = int(input("Digite a idade: "))
        idades.append(idade)

        altura = float(input("Digite a altura: "))
        alturas.append(altura)

        peso = float(input("Digite o peso: "))
        pesos.append(peso)

        total_pessoas_cadastradas += 1

        flag_two = True
        while flag_two:
            try:
                op = int(input("Dados cadastrados. Deseja adicionar mais dados? (1.Sim 2.Não): "))
                if op == 1:
                    flag_two = False
                elif op == 2:
                    flag_two = False
                    flag = False  # encerra o programa
                else:
                    print("Digite 1 para adicionar mais dados ou 2 para fechar o programa.")
            except ValueError:
                print("Digite apenas números (1 ou 2).")

    except ValueError:
        print("ERRO! Digite valores numéricos válidos para idade, altura e peso.")


media_idade = sum(idades) / len(idades)
media_peso = sum(pesos) / len(pesos)
media_altura = sum(alturas) / len(alturas)
porcentagem_feminino = (total_sexo_feminino / total_pessoas_cadastradas) * 100
porcentagem_masculino = (total_sexo_masculino / total_pessoas_cadastradas) * 100


print(f"A media da idade dos participantes é: {media_idade:.2f}")
print(f"A media do peso dos participantes é: {media_peso:.2f}")
print(f"A media da altura dos participantes é: {media_altura:.2f}")
print(f"A porcentagem total do sexo feminino é: {porcentagem_feminino:.2f}")
print(f"A porcentagem total do sexo masculino é: {porcentagem_masculino:.2f}")
print(f"A quantidade de pessoas com olhos verdes e cabelos louros: {caracteristicas_verificador}")