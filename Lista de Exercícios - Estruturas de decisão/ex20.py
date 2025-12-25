n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = int(input("Digite o terceiro número inteiro: "))
n4 = int(input("Digite o quarto número inteiro: "))

soma_n1_n2 = n1 + n2
soma_n3_n4 = n3 + n4

if soma_n1_n2 == soma_n3_n4:
    print("A soma dos dois primeiros valores é igual a soma dos dois últimos valores.")
    print(f"Os valores e a soma dos primeiros valores são: {n1} + {n2} = {soma_n1_n2}")
    print(f"Os valores e a soma dos últimos valores são: {n3} + {n4} = {soma_n3_n4}")
else:
    if soma_n1_n2 % 2 == 0:
        print("A soma dos dois primeiros valores é PAR")
    else:
        print("A soma dos dois primeiros valores é ÍMPAR")

    if soma_n3_n4 % 2 == 0:
        print("A soma dos dois últimos valores é PAR")
    else:
        print("A soma dos dois últimos valores é ÍMPAR")