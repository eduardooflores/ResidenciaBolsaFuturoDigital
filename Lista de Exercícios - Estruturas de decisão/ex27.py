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