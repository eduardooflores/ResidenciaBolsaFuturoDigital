nome = input("Digite o nome do cliente: ").upper()
valor = float(input("Digite o valor da conta: R$"))
inicial = nome[0]

iniciais = ['A', 'D', 'M', 'S']

if inicial in iniciais:
    desconto = valor * 0.30
    total = valor - desconto
    print(f"{nome}, seu nome está entre os descontos! O valor total fica: R${total:.2f}")
else:
    print("Que pena. Nesta semana o desconto não é para o seu nome. Mas continue nos prestigiando que sua vez chegará.")
