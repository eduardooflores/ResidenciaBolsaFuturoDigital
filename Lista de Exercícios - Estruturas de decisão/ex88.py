n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
n3 = float(input("Digite o terceiro valor: "))

valores = [n1, n2, n3]

valores.sort(reverse=True)

soma = valores[0] + valores[1]

print("A soma dos dois maiores valores é:", soma)
