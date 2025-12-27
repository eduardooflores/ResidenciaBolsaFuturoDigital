genero = input("Qual é o seu sexo: (1.Homem 2.Mulher): ")
idade = int(input("Digite a sua idade: "))
peso = float(input("Digite seu peso: "))
jejum = input("Está em jejum ? (1.Sim 2.Não): ")
documento = input("Possui documento com foto ? (1.Sim 2.Não): ")
hepatite = input("Você teve hepatite após os 10 anos ? (1.Sim 2.Não): ")
malaria = input("Você teve malária ? (1.Sim 2.Não): ")
dias_ultima_doacao = int(input("Digite quantos dias faz que você doou sangue: "))

if idade >= 18 and idade <= 67:
    if peso > 50:
        if jejum == "1":
            if documento == "1":
                if hepatite == "2":
                    if malaria == "2":
                        if genero == "1" and dias_ultima_doacao >= 60:
                            print("Pode doar sangue! Todos os requisitos aceitos")
                        elif genero == "2" and dias_ultima_doacao >= 90:
                            print("Pode doar sangue! Todos os requisitos aceitos")
                        else:
                            print("Não pode doar sangue! Dias desde a última doação inválido ou genero inválido")
                    else:
                        print("Não pode doar sangue! Malária impossibilita a doação de sangue")
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