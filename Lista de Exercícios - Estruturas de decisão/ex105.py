retorno_incuido = input("A viagem incluir retorno (S - SIM, N - NÃO): ").upper()
destino = input("Insira a região de destino: ").title()

regioes = {
    'Região Norte': (500, 900),
    'Região Nordeste': (350, 650),
    'Região Centro-Oeste': (350, 600),
    'Região Sudeste': (300, 500),
    'Região Sul': (300, 550),
}

if destino in regioes:
    valor_ida, valor_volta = regioes[destino]

    if retorno_incuido == "S":
        valor_total = valor_ida + valor_volta
    elif retorno_incuido == "N":
        valor_total = valor_ida
    else:
        print("Opção inválida para retorno!")
        valor_total = None

    if valor_total is not None:
        print(f"O total da viagem para {destino} é R${valor_total:.2f}")
else:
    print("Destino inválido!")
