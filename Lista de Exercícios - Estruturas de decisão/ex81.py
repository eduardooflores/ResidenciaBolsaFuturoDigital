print("Tabela de Conversão: Celsius para Fahrenheit")
print("---------------------------------------------")
print("Celsius\tFahrenheit")

for celsius in range(0, 41, 2):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}\t{fahrenheit:.1f}")
