flag = True
numeros_validos = []
dentro_intervalo = 0
fora_intervalo = 0

while flag:
    try:
        numeros = input("Digite 10 números separados por espaço: ").split()

        if len(numeros) != 10:
            print("Você deve digitar exatamente 10 números!")
            continue

        lista_numeros = list(map(int, numeros))

        for numero in lista_numeros:
            if 20 <= numero <= 50:
                dentro_intervalo += 1
                if numero % 2 == 0:
                    numeros_validos.append(numero)
            else:
                fora_intervalo += 1

        if numeros_validos:  # evita divisão por zero
            media = sum(numeros_validos) / len(numeros_validos)
        else:
            media = 0

        flag = False
    except:
        print("ERRO! DADOS INVÁLIDOS DIGITE NÚMEROS")

print(f"A média dos valores pares no intervalo é: {media}")
print(f"O total de valores dentro do intervalo é: {dentro_intervalo}")
print(f"O total de valores fora do intervalo é: {fora_intervalo}")
