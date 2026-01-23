farenheit = float(input("Digite a temperatura em Farenheit: "))
celcius = 5 / 9 * (farenheit - 32)

if celcius > 1:
    print("O tempo está agradável")
else:
    print("Está ficando frio")