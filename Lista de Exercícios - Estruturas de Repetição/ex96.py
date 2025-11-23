flag = True

while flag:
    try:
        flag_n1 = True
        while flag_n1:
            try:
                n1 = int(input("Digite a primeira nota: "))
                if n1 >= 0 and n1 <= 10:
                    flag_n1 = False  # sai do loop da primeira nota
                else:
                    print("Nota inválida. Digite entre 0 e 10.")
            except ValueError:
                print("ERRO! Digite apenas números entre 0 e 10.")

        flag_n2 = True
        while flag_n2:
            try:
                n2 = int(input("Digite a segunda nota: "))
                if n2 >= 0 and n2 <= 10:
                    flag_n2 = False
                else:
                    print("Nota inválida. Digite entre 0 e 10.")
            except ValueError:
                print("ERRO! Digite apenas números entre 0 e 10.")

        media = (n1 + n2) / 2
        print(f"{media:.1f} (média)")

    except ValueError:
        print("ERRO! DADOS INVÁLIDOS! DIGITE A NOTA ENTRE 0 E 10")

    flag_two = True

    while flag_two:
        try:
            op = int(input("Nova Cálculo (1.Sim 2.Não)? "))
            if op == 1:
                flag_two = False
                continue
            elif op == 2:
                flag_two = False
                flag = False
            else:
                print("Digite 1 para novo cálculo ou 2 para fechar o programa.")

        except ValueError:
            print("Digite valores entre 1 ou 2")