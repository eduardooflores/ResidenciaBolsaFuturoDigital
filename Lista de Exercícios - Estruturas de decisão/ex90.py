n1 = float(input("Digite a nota da primeira prova: "))
n2 = float(input("Digite a nota da segunda prova: "))
n3 = float(input("Digite a nota da terceira prova: "))

media = (n1 + n2 + n3) / 3

if media >= 7:
    print("Aprovado!")
else:
    print("Recuperação!")
    nota_necessaria = (7 - media * 0.60) / 0.40
    if nota_necessaria > 10:
        print("Infelizmente, mesmo com nota máxima na recuperação, não é possível ser aprovado.")
    else:
        print(f"Você precisa tirar pelo menos {nota_necessaria:.2f} na recuperação para ser aprovado.")
