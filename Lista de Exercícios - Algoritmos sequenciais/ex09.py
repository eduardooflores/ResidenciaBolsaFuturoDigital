# Q uestão 9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre
# a temperatura em graus Celsius. C = (5 * (F-32) / 9).

temperatura_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

temperatura_celsius = (5 * (temperatura_fahrenheit - 32) / 9)

print(temperatura_celsius)