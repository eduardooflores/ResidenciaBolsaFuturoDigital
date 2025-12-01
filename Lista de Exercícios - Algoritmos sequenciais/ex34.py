# ENTRADA
cotacao_dolar = float(input("Digite a cotação do dólar: "))
quantidade_dolar = float(input("Digite a quantidade de dólares a ser convertida: "))

# PROCESSAMENTO
dolar_para_real = quantidade_dolar * cotacao_dolar

# SAÍDA
print(f"A quantidade de U$ {quantidade_dolar:.2f}, convertida para real, fica: R$ {dolar_para_real:.2f}")
