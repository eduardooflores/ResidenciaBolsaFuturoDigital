classes = {
    1: {"nivel": "Excelente", "bonus": 1.00},
    2: {"nivel": "Bom", "bonus": 0.80},
    3: {"nivel": "Médio", "bonus": 0.50},
    4: {"nivel": "Regular", "bonus": 0.30},
    5: {"nivel": "Precisa treinar mais", "bonus": 0.10},
    6: {"nivel": "Te cuida", "bonus": 0.05},
    7: {"nivel": "Passe no Departamento Pessoal", "bonus": 0.00}
}

salario = float(input("Digite o salário do jogador: R$"))
classe = int(input("Digite o código da classe (1 a 7): "))

if classe in classes:
    nivel = classes[classe]["nivel"]
    bonus_percentual = classes[classe]["bonus"]
    salario_final = salario + (salario * bonus_percentual)

    print(f"Nível: {nivel}")
    print(f"Salário final: R${salario_final:.2f}")
else:
    print("Classe inválida. Digite um número entre 1 e 7.")
