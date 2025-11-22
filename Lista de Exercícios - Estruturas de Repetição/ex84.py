flag = True

while flag:
    try:
        nomes = input("Digite 8 nomes separados por espaço: ").split()

        if len(nomes) != 8:
            print("Você deve digitar exatamente 8 nomes!")
            continue

        # percorre cada nome e mostra quantas letras tem
        for nome in nomes:
            print(f"O nome '{nome}' tem {len(nome)} letras.")

        flag = False
    except:
        print("ERRO! DIGITE NOMES VÁLIDOS")
