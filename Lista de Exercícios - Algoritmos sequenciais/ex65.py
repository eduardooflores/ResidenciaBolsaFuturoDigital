#  Questão 65. O coração humano bate em média uma vez por segundo. Desenvolva um algoritmo
# para calcular e mostrar quantas vezes o coração de uma pessoa baterá se viver X anos. Considere
# como dado de entrada a idade da pessoa. Considerações: 1 ano = 365,25 dias, 1 dia = 24 horas, 1
# hora = 60 minutos e 1 minuto = 60 segundos

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