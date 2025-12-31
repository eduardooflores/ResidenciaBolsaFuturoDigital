from datetime import datetime
ANO = 2026

nascimento = input("Digite a sua da de nascimento (formato DD/MM/YYYY): ")
data_nascimento = datetime.strptime(nascimento, "%d/%m/%Y")

idade = ANO - data_nascimento.year

print(f"Em 2026 você terá: {idade} anos!")