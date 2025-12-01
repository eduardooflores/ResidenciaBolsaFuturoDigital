# ENTRADA
sigla_estado = input("Digite a sigla de um estado (RJ): ").upper()

# PROCESSAMENTO
if sigla_estado == 'RS':
    print(f"{sigla_estado} - gaúcho")
elif sigla_estado == 'RJ':
    print(f"{sigla_estado} - carioca")
elif sigla_estado == 'SP':
    print(f"{sigla_estado} - paulista")
elif sigla_estado == 'MG':
    print(f"{sigla_estado} - mineiro")
else:
    print("Outros estados")