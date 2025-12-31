from datetime import datetime

ano_atual = datetime.now().year
nascimento = input("Digite a sua da de nascimento (formato DD/MM/YYYY): ")
data_nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
idade = ano_atual - data_nascimento.year

if idade > 50:
    print(f"Você já tem {idade} anos, portanto mais de 50!")
elif idade < 50:
    anos_ate_50 = 50 - idade
    print(f"Você tem {idade} anos. Faltam {anos_ate_50} anos para chegar aos 50!")
else: print("Você tem exatamente 50 anos!")