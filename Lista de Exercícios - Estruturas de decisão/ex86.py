ANO = 2026

nome = input("Insira seu nome: ")
dia = int(input("Insira o dia do seu nascimento: "))
ano = int(input("Insira o ano de seu nascimento: "))
idade = ANO - ano

if idade >= 16:
    print("Pode votar!")
else:
    print("Não pode votar!")