total_escola = 0
total_alunos = 0

for turma in range(1, 6):
    try:
        n = int(input(f"Digite o número de alunos da turma {turma}: "))
    except ValueError:
        print("ERRO! Digite apenas números inteiros.")
        n = 0

    soma_turma = 0
    acima_7 = 0

    for aluno in range(1, n + 1):
        try:
            media_aluno = float(input(f"Digite a média do aluno {aluno} da turma {turma}: "))
            soma_turma += media_aluno
            total_escola += media_aluno
            total_alunos += 1

            if media_aluno > 7:
                acima_7 += 1
        except ValueError:
            print("ERRO! Digite apenas números válidos.")
            media_aluno = 0
            soma_turma += media_aluno
            total_escola += media_aluno
            total_alunos += 1

    print(f"Turma {turma}: {acima_7} alunos com média superior a 7")

media_escola = total_escola / total_alunos if total_alunos > 0 else 0
print(f"\nMédia geral da escola: {media_escola:.2f}")
