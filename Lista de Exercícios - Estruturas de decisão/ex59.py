soma = 0

for i in range(5):
    valor = int(input("Digite um valor de 0 até 10: "))
    soma += valor

media = soma / 5

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")
