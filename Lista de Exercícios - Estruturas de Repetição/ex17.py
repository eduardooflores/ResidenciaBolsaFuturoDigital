inicio = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))

if inicio > fim:
    print("Intervalo inválido! O valor inicial deve ser menor ou igual ao final.")
else:
    pares = []
    impares = []

    for num in range(inicio, fim + 1):
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    print(f"Valores no intervalo: {list(range(inicio, fim + 1))}")
    print(f"Quantidade de pares: {len(pares)}")
    print(f"Soma dos pares: {sum(pares)}")
    print(f"Quantidade de ímpares: {len(impares)}")
    if impares:
        print(f"Média dos ímpares: {sum(impares) / len(impares):.2f}")
    else:
        print("Não há ímpares no intervalo.")
