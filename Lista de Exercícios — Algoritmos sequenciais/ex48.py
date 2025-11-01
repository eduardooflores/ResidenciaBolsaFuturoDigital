# Entrada: hora e minuto
hora = int(input("Digite a hora (0 a 23): "))
minuto = int(input("Digite os minutos (0 a 59): "))

# Processamento: total de minutos desde o início do dia
total_minutos = hora * 60 + minuto

# Saída
print(f"Desde o início do dia se passaram {total_minutos} minutos.")
