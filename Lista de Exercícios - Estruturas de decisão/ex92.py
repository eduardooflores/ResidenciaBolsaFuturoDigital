n1 = float(input("Digite a nota a primeira avaliação: "))
n2 = float(input("Digite a nota a segunda avaliação: "))
n3 = float(input("Digite a nota a terceira avaliação: "))
n4 = float(input("Digite a nota a quarta avaliação: "))

media = (n1 + (n2 * 2) + (n3 * 3) + n4) / 7

if media >= 9:
    print("CONCEITO: A")
elif media >= 7.5 and media <= 8.9:
    print("CONCEITO: B")
elif media >= 6 and media <= 7.4:
    print("CONCEITO: C")
elif media >= 4 and media <= 5.9:
    print("CONCEITO: D")
else:
    print("CONCEITO: E")