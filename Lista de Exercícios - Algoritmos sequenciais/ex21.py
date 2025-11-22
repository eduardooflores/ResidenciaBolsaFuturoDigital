# Questão 21. Um colega pediu dinheiro emprestado, você aceitou emprestar com a condição de
# que ele irá devolver o valor emprestado com juros de 15%. Qual o valor que o colega pediu e quanto
# ele irá devolver depois?

# ENTRADA
valor_emprestado = 10

# PROCESSAMENTO
juros = 0.15
valor_juros = valor_emprestado * juros
total = valor_emprestado + valor_juros

# SAÍDA
print(f"O valor total a ser paga é de: R${total}")