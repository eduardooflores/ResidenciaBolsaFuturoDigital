sexo = input("Digite seu sexo (M - Masculino, F - Feminino): ").upper()
altura = float(input("Digite sua altura: "))

peso_ideal_homens = (72.7 * altura) - 58
peso_ideal_mulheres = (62.1 * altura) - 44.7

if sexo == "M":
    print(f"Para um homem com {altura:.2f}m, o peso ideal é {peso_ideal_homens:.2f} kg.")
elif sexo == "F":
    print(f"Para uma mulher com {altura:.2f}m, o peso ideal é {peso_ideal_mulheres:.2f} kg.")
else:
    print("Entrada inválida. Digite M para masculino ou F para feminino.")

