SENHA = 123456

acesso = int(input("Insira a senha: "))

if acesso != SENHA:
    print("ACESSO NEGADO")
else:
    print("ACESSO PERMITIDO")