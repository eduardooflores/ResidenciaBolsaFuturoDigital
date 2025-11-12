# Questão 70. Crie um algoritmo que leia uma hora do dia e informe quantos minutos se passaram
# desde o início do dia.

# ENTRADA
hora = int(input("Digite a hora do dia (0 a 23): "))

# PROCESSAMENTO
minutos_passados = hora * 60

# SAÍDA
print(f"Já se passaram {minutos_passados} minutos desde o início do dia.")
