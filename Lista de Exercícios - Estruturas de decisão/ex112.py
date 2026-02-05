nome = input("Digite o nome do pretendente: ").title()
idade = int(input("Digite a idade: "))
risco = input("Digite o grupo de risco (Baixo, Medio, Alto): ").strip().lower()

if idade < 17 or idade > 70:
    print(f"{nome}, idade {idade}: não está na faixa permitida para adquirir seguro.")
else:
    categoria = None

    if 17 <= idade <= 20:
        if risco == "baixo":
            categoria = 1
        elif risco == "medio":
            categoria = 2
        elif risco == "alto":
            categoria = 3

    elif 21 <= idade <= 24:
        if risco == "baixo":
            categoria = 2
        elif risco == "medio":
            categoria = 3
        elif risco == "alto":
            categoria = 4

    elif 25 <= idade <= 34:
        if risco == "baixo":
            categoria = 3
        elif risco == "medio":
            categoria = 4
        elif risco == "alto":
            categoria = 5

    elif 35 <= idade <= 64:
        if risco == "baixo":
            categoria = 4
        elif risco == "medio":
            categoria = 5
        elif risco == "alto":
            categoria = 6

    elif 65 <= idade <= 70:
        if risco == "baixo":
            categoria = 7
        elif risco == "medio":
            categoria = 8
        elif risco == "alto":
            categoria = 9

    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Categoria: {categoria}")
