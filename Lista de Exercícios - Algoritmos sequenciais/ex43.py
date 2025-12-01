# ENTRADA
VALOR_PAO = 0.12
VALOR_BROA = 1.50

qntd_paes_vendidos = int(input("Digite a quatidade de pães vendidos: "))
qntd_broa_vendidas = int(input("Digite a quantidade de boas vendidas: "))

# PROCESSAMENTO
total_paes_vendidos = qntd_paes_vendidos * VALOR_PAO
total_broa_vendidas = qntd_broa_vendidas * VALOR_BROA
total_arrecadado = total_paes_vendidos + total_broa_vendidas

poupanca = total_arrecadado * 0.10

# SAÍDA
print(f"O total arrecadado de pães e broas foi de: R$ {total_arrecadado:.2f}")
print(f"O valor de 10% do total arrecado para a poupança é de: R$ {poupanca:.2f}")