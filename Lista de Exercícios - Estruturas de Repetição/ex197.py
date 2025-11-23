total_turma = 0
alunos_maior_igual_5 = 0
medias_alunos = []

for i in range(1, 21):
    soma_notas = 0
    print(f"\nAluno {i}:")
    for j in range(1, 6):
        try:
            nota = float(input(f"Digite a {j}ª nota: "))
            soma_notas += nota
        except ValueError:
            print("ERRO! Digite apenas números.")
            nota = 0
            soma_notas += nota

    media_aluno = soma_notas / 5
    medias_alunos.append(media_aluno)
    total_turma += media_aluno

    print(f"Média do aluno {i}: {media_aluno:.2f}")

    if media_aluno >= 5:
        alunos_maior_igual_5 += 1

media_turma = total_turma / 20

alunos_acima_turma = sum(1 for m in medias_alunos if m > media_turma)

percentual_maior_igual_5 = (alunos_maior_igual_5 / 20) * 100

print("\n--- RESULTADOS ---")
print(f"Média da turma: {media_turma:.2f}")
print(f"Percentual de alunos com média >= 5: {percentual_maior_igual_5:.2f}%")
print(f"Quantidade de alunos com média maior que a média da turma: {alunos_acima_turma}")
