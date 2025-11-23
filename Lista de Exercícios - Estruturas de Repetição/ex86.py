from orca.messages import percentage

flag = True

while flag:
    try:
        numeros = input("Digite uma sequência de números: ").split()
        lista_numeros = list(map(int, numeros))

        maior_valor = max(lista_numeros)
        menor_valor = min(lista_numeros)
        soma_valores = sum(lista_numeros)
        media_valores = soma_valores / len(lista_numeros)
        numeros_maior_20 = 0
        numeros_maior_10 = 0
        soma_intervalo = 0
        qtd_intervalo = 0


        for numero in lista_numeros:
            if numero > 20:
                numeros_maior_20 += 1
            if numero > 10:
                numeros_maior_10 += 1
            if 10 <= numero <= 100:
                soma_intervalo += numero
                qtd_intervalo += 1

        if qtd_intervalo > 0:
            media_intervalo = soma_intervalo / qtd_intervalo
        else:
            media_intervalo = 0

        percentagem = (numeros_maior_10 / len(lista_numeros)) * 100

        flag = False
    except:
        print("ERRO! DIGITE NÚMEROS VÁLIDOS")

print(f"a) Maior valor: {maior_valor}")
print(f"b) Menor valor: {menor_valor}")
print(f"c) Soma dos valores: {soma_valores}")
print(f"d) Média dos valores: {media_valores:.2f}")
print(f"e) Quantos números maiores que 20: {numeros_maior_20}")
print(f"f) Percentagem de valores maiores que 10: {percentagem:.2f}%")
print(f"g) Média dos valores entre 10 e 100: {media_intervalo:.2f}")



