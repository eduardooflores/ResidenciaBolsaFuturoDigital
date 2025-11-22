validacao = True

while validacao:
    try:
        numeros = input("Digite 10 valores: ").split()
        contador_dentro_intervalo = 0
        contador_fora_intervalo = 0

        lista_numeros = list(map(int, numeros))

        if len(lista_numeros) != 10:
            codigo = 10
            raise ValueError()

        for i in lista_numeros:
            if i >= 10 and i <= 30:
                contador_dentro_intervalo += 1

            if i < 10 or i > 30:
                contador_fora_intervalo += 1

        validacao = False
    except:
        if codigo == 10:
            print("Lista com tamanho inválido")
        else:
            print("ERRO! DADOS INVÁLIDOS")

print(f"{contador_dentro_intervalo} Estão no invervalo")
print(f"{contador_fora_intervalo} Não estão no intervalo")