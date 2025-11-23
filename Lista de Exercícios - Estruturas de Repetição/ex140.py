for aluno in range(1, 11):
    soma_notas = 0
    print(f"\nAluno {aluno}:")
    for i in range(1, 6):
        try:
            nota = float(input(f"Digite a {i}ª nota: "))
            soma_notas += nota
        except ValueError:
            print("ERRO! Digite apenas números.")
            nota = 0
            soma_notas += nota

    media = soma_notas / 5

    if 0.1 <= media <= 2:
        situacao = "Nota PÉSSIMA"
    elif 2.1 <= media <= 4:
        situacao = "Nota MUITO RUIM"
    elif 4.1 <= media <= 6:
        situacao = "Nota de quem NÃO ESTUDOU O SUFICIENTE"
    elif 6.1 <= media <= 7:
        situacao = "Nota NO LIMITE"
    elif 7.1 <= media <= 8:
        situacao = "Nota BOA, pode melhorar"
    elif 8.1 <= media <= 9:
        situacao = "Nota MUITO BOA!"
    elif 9.1 <= media <= 9.7:
        situacao = "Nota QUASE EXCELENTE!"
    elif media > 9.8:
        situacao = "Nota na DISPUTA PELA COXINHA! :-)"
    else:
        situacao = "Nota fora da classificação"

    print(f"Média do aluno {aluno}: {media:.2f} - {situacao}")
