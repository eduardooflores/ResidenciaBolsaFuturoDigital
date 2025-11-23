total_veiculos = 0
total_acidentes_RS = 0
cidades_RS = 0

maior_indice = None
cidade_maior = None

menor_indice = None
cidade_menor = None

for i in range(1, 201):
    try:
        codigo = int(input(f"\nDigite o código da cidade {i}: "))
        estado = input("Digite o estado (ex: RS, SC, PR, SP, RJ...): ").upper()
        veiculos = int(input("Digite o número de veículos de passeio em 2018: "))
        acidentes = int(input("Digite o número de acidentes com vítimas em 2018: "))

        total_veiculos += veiculos

        if maior_indice is None or acidentes > maior_indice:
            maior_indice = acidentes
            cidade_maior = codigo

        if menor_indice is None or acidentes < menor_indice:
            menor_indice = acidentes
            cidade_menor = codigo

        if estado == "RS":
            total_acidentes_RS += acidentes
            cidades_RS += 1

    except ValueError:
        print("ERRO! Digite valores numéricos válidos para código, veículos e acidentes.")


media_veiculos = total_veiculos / 200
media_acidentes_RS = total_acidentes_RS / cidades_RS if cidades_RS > 0 else 0

print("\n--- RESULTADOS ---")
print(f"a) Maior índice de acidentes: {maior_indice} (Cidade código {cidade_maior})")
print(f"   Menor índice de acidentes: {menor_indice} (Cidade código {cidade_menor})")
print(f"b) Média de veículos nas cidades brasileiras: {media_veiculos:.2f}")
print(f"c) Média de acidentes com vítimas nas cidades do RS: {media_acidentes_RS:.2f}")
