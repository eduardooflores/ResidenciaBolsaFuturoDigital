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

