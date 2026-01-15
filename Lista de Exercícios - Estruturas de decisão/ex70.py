numero_secreto = int(input("Digite o número secreto: "))
acertou = False

for tentativa in range(3):
    adivinha = int(input("Tente adivinhar o número secreto: "))
    if adivinha < numero_secreto:
        print("O número secreto é maior!")
    elif adivinha > numero_secreto:
        print("O número secreto é menor!")
    else:
        print(f"Acertou! O número secreto é {numero_secreto}")
        acertou = True

if not acertou:
    print(f"Perdeu! O número secreto era: {numero_secreto}")
