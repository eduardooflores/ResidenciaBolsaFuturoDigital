# Questão 60. Faça um algoritmo onde o usuário digita 3 notas e seu nome. O programa deverá
# calcular a média das notas e mostrar seu nome e a média com a mensagem:
# • Inferior a 6,0 - Reprovado, faltou estudo!!!
    # • 6,1 a 6,9 - Recuperação, pode melhorar
# • 7,0 a 8,0 - Aprovado, mas não ganha coxinha
# • 8,1 a 9,7 – "Aprovado!"
# • 9,8 a 10 - "Aprovado, levando a coxinha no final do semestre":-)"

# ENTRADA
nome = input("Digite seu nome: ")
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

# PROCESSAMENTO
media = (nota_1 + nota_2 + nota_3) / 3

# SAÍDA
print(f"\nAluno: {nome}")
print(f"Média: {media:.2f}")

if media < 6.0:
    print("Reprovado, faltou estudo!!!")
elif 6.0 <= media <= 6.9:
    print("Recuperação, pode melhorar")
elif 7.0 <= media <= 8.0:
    print("Aprovado, mas não ganha coxinha")
elif 8.1 <= media <= 9.7:
    print("Aprovado!")
elif 9.8 <= media <= 10.0:
    print("Aprovado, levando a coxinha no final do semestre :-)")
else:
    print("Média inválida")
