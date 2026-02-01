valor_conta = float(input("Insira a valor total da conta: R$"))
qntd_amigos = int(input("Insira a quantidade de amigos: "))

if valor_conta < 300:
    porcentagem_joao = valor_conta * 0.8
    resto = valor_conta - porcentagem_joao
    valor_por_amigo = resto / qntd_amigos
    print(f"João paga: R${porcentagem_joao:.2f}")
    print(f"Cada amigo paga: R${valor_por_amigo:.2f}")
elif valor_conta > 300 and valor_conta < 600:
    porcentagem_joao = valor_conta / 2
    resto = valor_conta - porcentagem_joao
    valor_por_amigo = resto / qntd_amigos
    print(f"João paga: R${porcentagem_joao:.2f}")
    print(f"Cada amigo paga: R${valor_por_amigo:.2f}")
else:
    total_por_pessoa = valor_conta / (qntd_amigos + 1)
    print(f"Cada um paga: R${total_por_pessoa:.2f}")