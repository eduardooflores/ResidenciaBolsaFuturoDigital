nota_trabalho = float(input("Digite a nota do trabalho: "))
nota_prova = float(input("Digite a nota da prova: "))

peso_trabalho = nota_trabalho * 0.25
peso_prova = nota_prova * 0.75

nota_final = peso_prova + peso_trabalho

if nota_final < 7:
    print("Precisa de exame.")
else:
    print(f"Passaste com nota {nota_final:.2f}.")
