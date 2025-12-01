# ENTRADA
nome = input("Digite seu nome: ")
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

# PROCESSAMENTO
media = (nota_1 + nota_2 + nota_3) / 3

# SAÍDA
print(f"\nAluno: {nome}")
print(f"Média: {media:.2f}")

if media < 6.0:
    print("Reprovado, faltou estudo!!!")
elif 6.0 <= media <= 6.9:
    print("Recuperação, pode melhorar")
elif 7.0 <= media <= 8.0:
    print("Aprovado, mas não ganha coxinha")
elif 8.1 <= media <= 9.7:
    print("Aprovado!")
elif 9.8 <= media <= 10.0:
    print("Aprovado, levando a coxinha no final do semestre :-)")
else:
    print("Média inválida")
