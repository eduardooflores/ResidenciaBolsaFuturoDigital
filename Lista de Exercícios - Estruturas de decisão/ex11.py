n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
soma = n1 + n2

if soma > 20:
    total = soma + 8
    print(f"O total é: {total}")
else:
    total = soma - 5
    print(f"O total é: {total}")