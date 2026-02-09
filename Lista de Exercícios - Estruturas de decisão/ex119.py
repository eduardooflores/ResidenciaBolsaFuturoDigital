def identificar_animal():
    print("Responda às perguntas com SIM ou NÃO.")

    mamifero = input("É mamífero? ").strip().upper()
    if mamifero == "SIM":
        quadrupede = input("É quadrúpede? ").strip().upper()
        if quadrupede == "SIM":
            carnivoro = input("É carnívoro? ").strip().upper()
            if carnivoro == "SIM":
                return "Leão"
            else:
                return "Cavalo"
        else:
            bipede = input("É bípede? ").strip().upper()
            if bipede == "SIM":
                onivoro = input("É onívoro? ").strip().upper()
                if onivoro == "SIM":
                    return "Homem"
                else:
                    return "Macaco"
            else:
                voador = input("É voador? ").strip().upper()
                if voador == "SIM":
                    return "Morcego"
                else:
                    return "Baleia"

    ave = input("É ave? ").strip().upper()
    if ave == "SIM":
        voadora = input("É voadora? ").strip().upper()
        if voadora == "NÃO":
            tropical = input("Vive em região tropical? ").strip().upper()
            if tropical == "SIM":
                return "Avestruz"
            else:
                return "Pinguim"
        else:
            nadadora = input("É nadadora? ").strip().upper()
            if nadadora == "SIM":
                return "Pato"
            else:
                return "Águia"

    reptil = input("É réptil? ").strip().upper()
    if reptil == "SIM":
        casco = input("Tem casco? ").strip().upper()
        if casco == "SIM":
            return "Tartaruga"
        else:
            patas = input("Tem patas? ").strip().upper()
            if patas == "SIM":
                return "Crocodilo"
            else:
                return "Cobra"

    return "Animal não identificado."


animal = identificar_animal()
print(f"O animal escolhido foi: {animal}")
