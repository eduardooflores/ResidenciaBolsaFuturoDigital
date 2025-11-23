try:
    n = int(input("Digite o número de alunos da turma: "))

    aprovados = 0
    reprovados = 0
    exame = 0
    soma_aprovados = 0
    maior_nota = 0
    aprovados_maior_8 = 0

    for i in range(1, n + 1):
        print(f"\nAluno {i}:")
        try:
            nota1 = float(input("Digite a 1ª nota: "))
            nota2 = float(input("Digite a 2ª nota: "))
        except ValueError:
            print("ERRO! Digite apenas números.")
            nota1, nota2 = 0, 0

        media = (nota1 + nota2) / 2

        if media > maior_nota:
            maior_nota = media

        if media >= 6.0:
            aprovados += 1
            soma_aprovados += media
            if media > 8.0:
                aprovados_maior_8 += 1
        elif media < 4.0:
            reprovados += 1
        else:
            exame += 1

        print(f"Média do aluno {i}: {media:.2f}")

    media_aprovados = soma_aprovados / aprovados if aprovados > 0 else 0

    percentual_reprovados = (reprovados / n) * 100

    print("\n--- RESULTADOS ---")
    print(f"a) Número de alunos aprovados: {aprovados}")
    print(f"b) Número de alunos reprovados: {reprovados}")
    print(f"c) Número de alunos em exame: {exame}")
    print(f"d) Média das notas finais dos aprovados: {media_aprovados:.2f}")
    print(f"e) Percentual de reprovados: {percentual_reprovados:.2f}%")
    print(f"f) Maior nota da turma: {maior_nota:.2f}")
    print(f"g) Alunos aprovados com média > 8: {aprovados_maior_8}")

except ValueError:
    print("ERRO! Digite um número inteiro válido para a quantidade de alunos.")
