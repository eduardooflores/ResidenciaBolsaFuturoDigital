# Questão 27. Para doar sangue é necessário ter entre 18 e 67 anos e pesar mais de 50kg. Faça um
# programa que pergunta a idade e o peso do usuário e diga se ele pode doar sangue ou não.

# ENTRADA
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))

# PROCESSAMENTO
if idade < 18 or idade > 67:
    print("Você não pode duar sangue. Não possuí a idade adequada.")
else:
    if peso < 50:
        print("Você não pode duar sangue. Não possuí o peso adequado.")
    else:
        print("Você pode duar sangue!")