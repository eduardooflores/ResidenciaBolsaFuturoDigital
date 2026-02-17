try:
    inicio_intervalo = int(input("Insira um valor de início: "))
    fim_intervalor = int(input("Insira um valor de fim: "))

    for numeros in range(inicio_intervalo, fim_intervalor + 1):
        print(numeros)

except ValueError:
    print("ERRO! Os dados devem ser números.")