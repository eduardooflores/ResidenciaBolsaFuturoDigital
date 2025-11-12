# Questão 36. Faça um programa que leia um número de DDI e indique o nome do país
# correspondente ao DDI. Por exemplo: Digite 1 e o nome do país será "Estados Unidos"; Digitando
# 49 o nome do país será "Alemanha"; O número 55 mostrará o "Brasil". Caso o usuário digite um
# número não cadastrado, mostre a mensagem "DDI não existe".

# ENTRADA
ddi = int(input("Digite um número de DDI: "))

# PROCESSAMENTO
if ddi == 1:
    print("Estados Unidos")
elif ddi == 49:
    print("Alemanha")
elif ddi == 55:
    print("Brasil")
else:
    print("DDI não existe")