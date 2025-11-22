# Q uestão 12. Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um
# algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: Para homens: (72.7*h) – 58
# Para mulheres: (62.1*h) - 44.7 (h = altura) Peça o peso da pessoa e informe se ela está dentro, acima
# ou abaixo do peso.

altura = float(input("Digite a altura da pessoa: "))
sexo = input("Digite o sexo da pessoa (M/F): ").upper()
peso = float(input("Digite o peso da pessoa: "))

FORMULA_HOMEM = (72.7 * altura) - 58
FORMULA_MULHER = (62.1 * altura) - 44.7

# PROCESSAMENTO
verifica_sexo_masculino = (sexo == "M")
verifica_sexo_feminino = (sexo == "F")

peso_ideal_homem = (peso == FORMULA_HOMEM) * 1
peso_acima_homem = (peso > FORMULA_HOMEM) * 1
peso_abaixo_homem = (peso < FORMULA_HOMEM) * 1

peso_ideal_mulher = (peso == FORMULA_MULHER) * 1
peso_acima_mulher = (peso > FORMULA_MULHER) * 1
peso_abaixo_mulher = (peso < FORMULA_MULHER) * 1

verifica_peso_ideal_homem = verifica_sexo_masculino and peso_ideal_homem and print("Peso ideal")
verifica_peso_abaixo_homem = verifica_sexo_masculino and peso_abaixo_homem and print("Peso abaixo do ideal")
verifica_peso_acima_homem = verifica_sexo_masculino and peso_acima_homem and print("Peso acima do ideal")

verifica_peso_ideal_mulher = verifica_sexo_feminino and peso_ideal_mulher and print("Peso ideal")
verifica_peso_abaixo_mulher = verifica_sexo_feminino and peso_abaixo_mulher and print("Peso abaixo do ideal")
verifica_peso_acima_mulher = verifica_sexo_feminino and peso_acima_mulher and print("Peso acima do ideal")