# Questão 91. Faça um algoritmo que leia 5 notas obtidas por um aluno em 5 avaliações. Calcule a
# média usando a seguinte equação:
# • Média = ( N1 + N2 + N3 + N4 + N5) / 5
# • A seguir mostre a média e a situação do aluno baseado na tabela:
# Nota/Média  Situação
# 0,1 a 2     Nota PÉSSIMA
# 2,1 a 4     Nota MUITO RUIM
# 4,1 a 6     Nota de quem NÃO ESTUDOU O SUFICIENTE
# 6,1 a 7     Nota NO LIMITE
# 7,1 a 8     Nota BOA, pode melhorar
# 8,1 a 9     Nota MUITO BOA!
# 9,1 a 9,7   Nota QUASE EXCELENTE
# Acima de 9,8 Nota na DISPUTA PELA COXINHA! :-)

# ENTRADA
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))
n5 = float(input("Digite a quinta nota: "))

# PROCESSAMENTO
media = (n1 + n2 + n3 + n4 + n5) / 5
print(f"Média: {media:.2f}")

if 0.1 <= media <= 2.0:
    print("NOTA PÉSSIMA")
elif 2.1 <= media <= 4.0:
    print("NOTA MUITO RUIM")
elif 4.1 <= media <= 6.0:
    print("NOTA DE QUEM NÃO ESTUDOU O SUFICIENTE")
elif 6.1 <= media <= 7.0:
    print("NOTA NO LIMITE")
elif 7.1 <= media <= 8.0:
    print("NOTA BOA, PODE MELHORAR")
elif 8.1 <= media <= 9.0:
    print("NOTA MUITO BOA!")
elif 9.1 <= media <= 9.7:
    print("NOTA QUASE EXCELENTE")
elif media > 9.8:
    print("NOTA NA DISPUTA PELA COXINHA! :-)")
else:
    print("Média fora da faixa avaliada.")

