flag = True
numeros_validos = 0

while flag:
    try:
        numeros = input("Digite 10 números separados por espaço: ").split()

        if len(numeros) != 10:
            print("Você deve digitar exatamente 10 números!")
            continue

        lista_numeros = list(map(int, numeros))

        for numero in lista_numeros:
            if numero % 2 == 0:
                if (10 <= numero <= 50) or (100 <= numero <= 200):
                    numeros_validos += 1
        flag = False
    except:
        print("ERRO! DADOS INVÁLIDOS! DIGITE NÚMEROS INTEIROS")

print(f"Quantidade de números pares dentro dos intervalos: {numeros_validos}")
