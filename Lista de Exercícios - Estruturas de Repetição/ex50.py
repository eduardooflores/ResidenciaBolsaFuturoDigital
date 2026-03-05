valores = []
flag = True

for i in range(4):
    while flag:
        try:
            valor = int(input(f"Digite o {i+1}º valor inteiro: "))
            valores.append(valor)
            break
        except ValueError:
            print("ERRO! Digite um número inteiro válido.")

menor_valor = min(valores)

print(f"O menor valor digitado foi: {menor_valor}")
