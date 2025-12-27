idade = int(input("Digite a sua idade: "))
peso = float(input("Digite o seu peso: "))
jejum = input("Está em jejum ? (1.Sim 2.Não): ")
documento = input("Possui documento com foto ? (1.Sim 2.Não): ")
hepatite = input("Você teve hepatite após os 10 anos? (1.Sim 2.Não): ")

if idade >= 18 and idade <= 67:
    if peso > 50:
        if jejum == "1":
            if documento == "1":
                if hepatite == "2":
                    print("Pode doar sangue! Todos os requisitos aceitos")
                else:
                    print("Não pode doar sangue! Hepatite após os 10 anos")
            else:
                print("Não pode doar sangue! Deve possuir documento com foto")
        else:
            print("Não pode doar sangue! Deve estar em jejum")
    else:
        print("Não pode doar sangue! Peso inválido")
else:
    print("Não pode doar sangue! Idade inválida")