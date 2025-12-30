CAPITAL = "PORTO ALEGRE"
TENTATIVAS = 3

for tentativa in range(1, TENTATIVAS + 1):
    adivinha = input("Adivinhe a capital do brasil: ").strip().upper()

    if adivinha == CAPITAL:
        print("Parabéns! Você acertou!")
        print("Porto Alegre tem a maior pista de skate da américa latina!")
        break
    else:
        if tentativa == 1:
            print("ERRADO! Tem mais duas tentativas!")
            print("DICA: Começa com PORTO")
        elif tentativa == 2:
            print("ERRADO! Tem mais uma tentativa!")
            print("DICA: E uma capital ALEGRE")
        else:
            print("Você errou em todas as tentavias!")
            print(f"A resposta correta era: {CAPITAL}")
