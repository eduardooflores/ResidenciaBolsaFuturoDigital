#  Questão 23. Calcula a média das notas de Algoritmos e Lógica de Programação. Assuma que serão
# fornecidas 4 diferentes notas (2 trabalhos e 2 provas). Observe que as provas equivalem a 60% da
# nota final, enquanto que os trabalhos equivalem a 40% da nota final. Nota final = (Prova 1 + Prova
# 2) * 0,60 + (Trabalho 1 + Trabalho 2) * 0,40.

# ENTRADA
primeiro_trabalho = 10
segundo_trabalho = 0
primera_prova = 10
segunda_prova = 10

# PROCESSAMENTO
nota_final = (primera_prova + segunda_prova) * 0.60 + (primeiro_trabalho + segundo_trabalho) * 0.40

# SAÍDA
print(f"A nota final do aluna é de: {nota_final}")