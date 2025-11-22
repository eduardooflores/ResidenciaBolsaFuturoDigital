#  print("Programa para calcular o valor total da conta de luz!")

id_cliente = input("Digite seu ID: ")
leitura_anterior = int(input("Digite a leitura anterior do medidor em kWh: "))
leitura_atual = int(input("Digite a leitura atual do medidor em kWh: "))
tarifa_bandeira = float(input("Digite a tarifa da bandeira em reais por kWh: " ))
custo_distribuicao = float(input("Digite o custo de distribição em reais por kWh: "))
valor_iluminacao = float(input("Digite o valor da iluminação pública em reais: "))

#  PROGRAMA

consumo = leitura_atual - leitura_anterior
valor_energia = consumo * tarifa_bandeira
valor_distribuicao = consumo * custo_distribuicao
total = valor_energia + valor_distribuicao + valor_iluminacao

#  SAÍDA

print(f"CLIENTE {id_cliente}:",f"CONSUMO {consumo} KWH")
print(f"ENERGIA: R$ {valor_energia:.2f}")
print(f"DISTRIBUIÇÃO: R$ {valor_distribuicao:.2f}")
print(f"ILUMINAÇÃO: R$ {valor_iluminacao:.2f}")
print(f"TOTAL: R$ {total:.2f}")