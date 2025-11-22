#  Questão 49. Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e
# mostre-a expressa apenas em dias.

# ENTRADA
anos = int(input("Digite sua idade em anos: "))
meses = int(input("Digite sua idade em meses: "))
dias = int(input("Digite sua idade em dias: "))

# PROCESSAMENTO
total_dias = anos * 365 + meses * 30 + dias

# SAÍDA
print(f"A sua idade em dias é de: {total_dias}")