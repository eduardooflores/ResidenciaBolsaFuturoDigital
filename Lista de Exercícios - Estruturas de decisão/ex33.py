ANO_ATUAL = 2025
ano_nascimento = int(input("Digite o ano em que nasceu: "))

if ano_nascimento > ANO_ATUAL:
    print("Ano de nascimento inválido!")
elif ano_nascimento < 1900:
    print("Ano de nascimento inválido!")
else:
    idade = ANO_ATUAL - ano_nascimento
    print(f"A sua idade é {idade}")