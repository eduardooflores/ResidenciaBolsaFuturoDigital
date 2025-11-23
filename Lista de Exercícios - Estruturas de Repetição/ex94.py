flag = True
SENHA = 2014
contador_tentativas = 0

while flag:
    try:
        senha = int(input("Digite a senha: "))

        if senha != 2014:
            contador_tentativas += 1
            print(f"{senha} SENHA INVÁLIDA")
        else:
            contador_tentativas += 1
            print(f"{senha} ACESSO PERMITIDO")
            flag = False
            print(f"Senha digitada {contador_tentativas}")
    except ValueError:
        print("ERRO! DADOS INVÁLIDOS! A SENHORA ACEIRA SOMENTA DADOS NUMÉRICOS")
