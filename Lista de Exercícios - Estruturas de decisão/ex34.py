valor = float(input("Digite o valor da prestação: "))
taxa = float(input("Digite a taxa da prestação: "))
tempo_atraso = int(input("Digite em meses o tempo de atraso da prestação: "))

prestacao = valor + (valor * taxa * tempo_atraso)

print(f"O valor total a pagar da prestação é de: R${prestacao:.2f}")