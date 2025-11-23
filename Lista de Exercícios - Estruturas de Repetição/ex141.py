medias_alunos = []
total_turma = 0

for aluno in range(1, 6):
    soma_notas = 0
    print(f"\nAluno {aluno}:")
    for i in range(1, 4):
        try:
            nota = float(input(f"Digite a {i}ª nota: "))
            soma_notas += nota
        except ValueError:
            print("ERRO! Digite apenas números.")
            nota = 0
            soma_notas += nota

    media_aluno = soma_notas / 3
    medias_alunos.append(media_aluno)
    total_turma += media_aluno

    if media_aluno >= 9.0:
        conceito = "A"
    elif 7.5 <= media_aluno <= 8.9:
        conceito = "B"
    elif 6.0 <= media_aluno <= 7.4:
        conceito = "C"
    elif 4.0 <= media_aluno <= 5.9:
        conceito = "D"
    else:
        conceito = "E"

    print(f"Média do aluno {aluno}: {media_aluno:.2f} - Conceito {conceito}")

media_geral = total_turma / 5

print("\n--- RESULTADOS ---")
print(f"Média geral da turma: {media_geral:.2f}")

if media_geral >= 9.0:
    mensagem = "Turma com desempenho EXCELENTE!"
elif 7.5 <= media_geral <= 8.9:
    mensagem = "Turma com bom desempenho."
elif 6.0 <= media_geral <= 7.4:
    mensagem = "Turma com desempenho regular."
elif 4.0 <= media_geral <= 5.9:
    mensagem = "Turma com desempenho fraco."
else:
    mensagem = "Turma com desempenho muito ruim."

print(mensagem)
