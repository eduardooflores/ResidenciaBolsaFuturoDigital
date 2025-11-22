# Qu estão 34. Elabore um algoritmo que converta um valor em dólar (U$) para real (R$).
# O algoritmo deverá solicitar o valor da cotação do dólar e também a quantidade de dólares a ser convertida.

# ENTRADA
cotacao_dolar = float(input("Digite a cotação do dólar: "))
quantidade_dolar = float(input("Digite a quantidade de dólares a ser convertida: "))

# PROCESSAMENTO
dolar_para_real = quantidade_dolar * cotacao_dolar

# SAÍDA
print(f"A quantidade de U$ {quantidade_dolar:.2f}, convertida para real, fica: R$ {dolar_para_real:.2f}")
