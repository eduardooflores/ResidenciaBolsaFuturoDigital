percurso_km = float(input("Digite o tamanho do percurso em quilômetros: "))
tipo_carro = input("Digite o tipo de carro (A - B - C): ").upper()

CARRO_A = 12
CARRO_B = 9
CARRO_C = 8

if tipo_carro == "A":
    consumo = percurso_km / CARRO_A
elif tipo_carro == "B":
    consumo = percurso_km / CARRO_B
elif tipo_carro == "C":
    consumo = percurso_km / CARRO_C
else:
    print("Tipo de carro inválido!")
    consumo = None

if consumo is not None:
    print(f"O consumo estimado de combustível é {consumo:.2f} litros.")
