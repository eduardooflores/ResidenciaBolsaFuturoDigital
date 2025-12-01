# ENTRADA
PRECO_CAMISA_P = 10
PRECO_CAMISA_M = 12
PRECO_CAMISA_G = 15

qntd_camisas_p = int(input("Digite a quantidade de camisas p compradas: "))
qntd_camisas_m = int(input("Digite a quantidade de camisas m compradas: "))
qntd_camisas_g = int(input("Digite a quantidade de camisas g compradas: "))

# PROCESSAMENTO
total_camisas_p = qntd_camisas_p * PRECO_CAMISA_P
total_camisas_m = qntd_camisas_m * PRECO_CAMISA_M
total_camisas_g = qntd_camisas_g * PRECO_CAMISA_G
total = total_camisas_p + total_camisas_m + total_camisas_g

# SAÍDA
print(f"O valor total arrecadodo com a venda das camisas é de: R$ {total}")