tipo = input("Digite o tipo de usuário (funcionario, financeiro, diretoria): ").lower()
hora = int(input("Digite a hora (0-23): "))
minuto = int(input("Digite os minutos (0-59): "))

minutos = hora * 60 + minuto

if tipo == "financeiro" or tipo == "diretoria":
    print("Acesso permitido")
elif tipo == "funcionario":
    if (0 <= minutos <= 450) or (1110 <= minutos <= 1440) or (720 <= minutos <= 810):
        print("Acesso permitido")
    else:
        print("Acesso negado")
else:
    print("Tipo de usuário inválido")
