# ENTRADA
altura = float(input("Digite a altura do atleta em metros (ex: 1.75): "))
peso = float(input("Digite o peso do atleta em kg: "))

# PROCESSAMENTO
altura_valida = altura >= 1.75 and altura <= 1.90
peso_valido = peso >= 70 and peso <= 80

if altura_valida and peso_valido:
    print("ACEITO")
elif not altura_valida and peso_valido:
    print("RECUSADO POR ALTURA")
elif altura_valida and not peso_valido:
    print("RECUSADO POR PESO")
else:
    print("TOTALMENTE RECUSADO")