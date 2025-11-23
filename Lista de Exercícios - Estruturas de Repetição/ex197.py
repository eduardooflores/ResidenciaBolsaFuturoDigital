try:
    n = int(input("Digite o número de alunos pesquisados: "))

    total_usaram = 0
    menos_5 = 0
    entre_5_10 = 0
    mais_10 = 0
    soma_utilizacao = 0
    maior = None
    menor = None

    for i in range(1, n + 1):
        try:
            uso = int(input(f"Digite a quantidade de vezes que o aluno {i} usou o Xerox: "))
        except ValueError:
            print("ERRO! Digite apenas números inteiros.")
            uso = 0

        if uso > 0:
            total_usaram += 1

        if uso < 5:
            menos_5 += 1
        elif 5 <= uso <= 10:
            entre_5_10 += 1
        else:
            mais_10 += 1

        soma_utilizacao += uso

        if maior is None or uso > maior:
            maior = uso
        if menor is None or uso < menor:
            menor = uso

    media = soma_utilizacao / n if n > 0 else 0
    perc_menos_5 = (menos_5 / n) * 100
    perc_entre_5_10 = (entre_5_10 / n) * 100
    perc_mais_10 = (mais_10 / n) * 100

    print("\n--- RESULTADOS ---")
    print(f"a) Total de alunos que usaram o Xerox: {total_usaram}")
    print(f"b) Percentual de alunos que usaram menos de 5 vezes: {perc_menos_5:.2f}%")
    print(f"c) Percentual de alunos que usaram entre 5 e 10 vezes: {perc_entre_5_10:.2f}%")
    print(f"d) Percentual de alunos que usaram mais de 10 vezes: {perc_mais_10:.2f}%")
    print(f"e) Quantidade total de vezes que os alunos usaram: {soma_utilizacao}")
    print(f"f) Média de utilização: {media:.2f}")
    print(f"g) Maior utilização: {maior}")
    print(f"   Menor utilização: {menor}")

except ValueError:
    print("ERRO! Digite um número válido de alunos.")
