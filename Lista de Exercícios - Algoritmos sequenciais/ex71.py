# Questão 71. Faça um algoritmo que lê o peso (só a parte inteira) e calcula:
# • o peso da pessoa em gramas
# • novo peso, considerando que a pessoa pode engordar 12%
# • novo peso, onde a pessoa passará o valor em % do que engordou

# ENTRADA
peso = int(input("Digite seu peso (em kg, parte inteira): "))

# PROCESSAMENTO
peso_gramas = peso * 1000
peso_engordar_12 = peso * 1.12  # aumento de 12%

# agora o usuário escolhe quanto quer engordar
percentual_engordar = float(input("Digite o percentual que deseja engordar (%): "))
peso_engordar_percentual = peso * (1 + percentual_engordar / 100)

# SAÍDA
print(f"Seu peso em gramas é: {peso_gramas} g")
print(f"Se engordar 12%, seu novo peso será: {peso_engordar_12:.2f} kg")
print(f"Se engordar {percentual_engordar:.1f}%, seu novo peso será: {peso_engordar_percentual:.2f} kg")