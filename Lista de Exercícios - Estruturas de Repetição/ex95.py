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

        flag = False

    except ValueError:
        print("ERRO! DADOS INVÁLIDOS! DIGITE A NOTA ENTRE 0 E 10")