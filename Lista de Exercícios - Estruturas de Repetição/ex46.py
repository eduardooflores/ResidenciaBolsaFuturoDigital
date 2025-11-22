validacao = True

while validacao:
    try:
        numeros = input("Digite 10 números inteiros: ").split()
        lista_numeros = list(map(int, numeros))

        maior_numero = max(lista_numeros)
        menor_numero = min(lista_numeros)

        validacao = False

    except:
        print("DADOS INVÁLIDOS! DIGITE NÚMEROS INTEIROS")

print(f"Lista de números: {lista_numeros}")
print(f"O maior número na lista é: {maior_numero}")
print(f"O menor número na lista é: {menor_numero}")
