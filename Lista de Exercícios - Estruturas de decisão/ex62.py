# Questão 62. Faça um programa para ler a idade de 5 alunos e mostrar um mensagem ao final de
# acordo com as instruções:
# • Se a média de idade dos alunos for inferior de 25, apresentar a mensagem "Turma Jovem"e
# a idade de cada aluno.
# • Se a média de idade dos alunos está entre 25 e 40, apresentar a mensagem "Turma
# Adulta"e a média das idades.
# • Se a média de idade dos alunos está acima de 40 anos, apresentar a mensagem "Turma
# Idosa", mostrar a média das idades e a idade de cada aluno.

# ENTRADA
idade_primeiro_aluno = int(input("Digite a idade do primeiro aluno: "))
idade_segundo_aluno = int(input("Digite a idade do segundo aluno: "))
idade_terceiro_aluno = int(input("Digite a idade do terceiro aluno: "))
idade_quarto_aluno = int(input("Digite a idade do quarto aluno: "))
idade_quinto_aluno = int(input("Digite a idade quinto aluno: "))

# PROCESSAMENTO
media_idade_alunos = (idade_primeiro_aluno + idade_segundo_aluno + idade_terceiro_aluno +
                      idade_quarto_aluno + idade_quinto_aluno) / 5

if media_idade_alunos < 25:
    print("Turma Jovem")
    print(f"O primeiro aluno tem {idade_primeiro_aluno} anos\n"
          f"O segundo aluno tem {idade_segundo_aluno} anos\n"
          f"O terceiro aluno tem {idade_terceiro_aluno} anos\n"
          f"O quarto aluno tem {idade_quarto_aluno} anos\n"
          f"O quinto aluno tem {idade_quinto_aluno} anos\n")

if media_idade_alunos >= 25 and media_idade_alunos <= 40:
    print("Turma Adulta")
    print(f"A media das idades é de: {media_idade_alunos:.2f}")

if media_idade_alunos > 40:
    print("Turma idosa")
    print(f"O primeiro aluno tem {idade_primeiro_aluno} anos\n"
          f"O segundo aluno tem {idade_segundo_aluno} anos\n"
          f"O terceiro aluno tem {idade_terceiro_aluno} anos\n"
          f"O quarto aluno tem {idade_quarto_aluno} anos\n"
          f"O quinto aluno tem {idade_quinto_aluno} anos\n")