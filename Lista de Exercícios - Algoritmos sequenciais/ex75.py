# ENTRADA
numero_conta = int(input("Digite o número da conta com três dígitos (exemplo: 235): "))

# PROCESSAMENTO
# Inverte o número (usando string, mas sem laço)
numero_inverso = int(str(numero_conta)[::-1])

# Soma número e seu inverso
soma_inverso = numero_conta + numero_inverso

# Quebrar a soma em dígitos (centena, dezena e unidade)
centena = soma_inverso // 100
dezena = (soma_inverso // 10) % 10
unidade = soma_inverso % 10

# Multiplicar cada dígito pela posição e somar
soma_posicional = (centena * 1) + (dezena * 2) + (unidade * 3)

# O último dígito é o verificador
digito_verificador = soma_posicional % 10

# SAÍDA
print(f"\nNúmero da conta: {numero_conta}")
print(f"Número inverso: {numero_inverso}")
print(f"Soma dos dois: {soma_inverso}")
print(f"Soma posicional: {soma_posicional}")
print(f"Dígito verificador: {digito_verificador}")