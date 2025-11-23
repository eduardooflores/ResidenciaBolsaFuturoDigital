candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
nulos = 0
brancos = 0

total_eleitores = 30

for i in range(1, total_eleitores + 1):
    try:
        voto = int(input(f"Digite o voto do eleitor {i} (1-4 candidatos, 5 nulo, 6 branco): "))
    except ValueError:
        print("ERRO! Digite apenas números inteiros.")
        voto = 0

    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    elif voto == 4:
        candidato4 += 1
    elif voto == 5:
        nulos += 1
    elif voto == 6:
        brancos += 1
    else:
        print("Código inválido! Voto desconsiderado.")

percentual_nulos_brancos = ((nulos + brancos) / total_eleitores) * 100

print("\n--- RESULTADOS ---")
print(f"a) Total de votos candidato 1: {candidato1}")
print(f"   Total de votos candidato 2: {candidato2}")
print(f"   Total de votos candidato 3: {candidato3}")
print(f"   Total de votos candidato 4: {candidato4}")
print(f"b) Total de votos nulos: {nulos}")
print(f"c) Total de votos em branco: {brancos}")
print(f"d) Percentual de votos nulos e brancos sobre o total: {percentual_nulos_brancos:.2f}%")
