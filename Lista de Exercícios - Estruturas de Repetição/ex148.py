maior_nota = None
menor_nota = None
total_reprovados = 0
total_maior_9 = 0
reprovados_frequencia = 0

for i in range(1, 21):
    print(f"\nAluno {i}:")
    matricula = input("Digite o número da matrícula: ")

    soma_notas = 0
    for j in range(1, 6):
        try:
            nota = float(input(f"Digite a {j}ª nota: "))
            soma_notas += nota
        except ValueError:
            print("ERRO! Digite apenas números.")
            nota = 0
            soma_notas += nota

    media = soma_notas / 5

    try:
        frequencia = int(input("Digite o número de aulas frequentadas: "))
    except ValueError:
        print("ERRO! Digite apenas números inteiros.")
        frequencia = 0

    if media >= 6 and frequencia >= 20:
        situacao = "APROVADO"
    else:
        situacao = "REPROVADO"
        total_reprovados += 1
        if frequencia < 20:
            reprovados_frequencia += 1

    if maior_nota is None or media > maior_nota:
        maior_nota = media
    if menor_nota is None or media < menor_nota:
        menor_nota = media

    if media > 9:
        total_maior_9 += 1

    print(f"Matrícula: {matricula} | Média: {media:.2f} | Situação: {situacao}")

percentual_reprovados_freq = (reprovados_frequencia / 20) * 100

print("\n--- RESULTADOS FINAIS ---")
print(f"Maior nota final da turma: {maior_nota:.2f}")
print(f"Menor nota final da turma: {menor_nota:.2f}")
print(f"Total de alunos reprovados: {total_reprovados}")
print(f"Total de alunos com nota final > 9: {total_maior_9}")
print(f"Percentual de reprovados por frequência insuficiente: {percentual_reprovados_freq:.2f}%")
