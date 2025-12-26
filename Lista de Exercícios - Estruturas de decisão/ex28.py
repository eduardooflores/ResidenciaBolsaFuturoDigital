idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
jejum = input("Está em jejum ? (1.Sim 2.Não): ")
documento = input("Possuí documento com foto ? (1.Sim 2.Não): ")

if idade >= 18 and idade <= 67:
    if peso > 50:
        if jejum == "1":
                print("Pode doar sangue!")
        else:
            print("Não pode doar sangue! Precisa estar em jejum!")
    else:
        print("Não pode doar sangue! Peso inválido!")
else:
    print("Não pode doar sangue! Idade inválida!")