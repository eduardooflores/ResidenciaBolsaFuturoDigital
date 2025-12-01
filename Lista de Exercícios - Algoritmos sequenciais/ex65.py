# ENTRADA
ANO = 365.25
DIA = 24
HORA = 60
MINUTO = 60

idade = int(input("Digite a sua idade: "))

# PROCESSAMENTO
idade_dias = idade * ANO
idade_horas = idade_dias * DIA
idade_minutos = idade_horas * HORA
idade_segundos = idade_minutos * MINUTO

# SAÍDA
print(f"Se você tem {idade} anos, seu coração já bateu aproximadamente {idade_segundos:,.0f} vezes.")