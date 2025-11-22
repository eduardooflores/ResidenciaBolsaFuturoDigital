flag = True
contador = 0

while flag:
    profissao = input("Digite uma profissão (ou 0 para sair): ")

    if profissao == "0":
        flag = False

    if profissao.upper() == "PROFESSOR":
        contador += 1

print(f"A profissão 'professor' foi digitada {contador} vezes.")