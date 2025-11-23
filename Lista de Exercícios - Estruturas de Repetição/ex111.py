flag = True

torcedores_inter = 0
torcedores_gremio = 0
torcedores_outro = 0
pessoas_entrevistadas = 0

while flag:
    try:
        clube = int(input("Digite o clube de preferência ou zero para sair (1-Grêmio;2-Internacional;3-Outros)"))
        if clube == 0:
            flag = False
            continue

        if clube == 1:
            torcedores_gremio += 1

        if clube == 2:
            torcedores_inter += 1

        cidade = int(input("Cidade de origem (0-Porto Alegre;1-Outras)"))
        if cidade == 0 and clube == 3:
            torcedores_outro += 1

        pessoas_entrevistadas += 1
    except ValueError:
        print("ERRO! DADOS INSERIDOS INVÁLIDOS!")


print("\n--- RESULTADOS ---")
print(f"Total de pessoas entrevistadas: {pessoas_entrevistadas}")
print(f"Torcedores do Grêmio: {torcedores_gremio}")
print(f"Torcedores do Internacional: {torcedores_inter}")
print(f"Torcedores de outros clubes: {torcedores_outro}")