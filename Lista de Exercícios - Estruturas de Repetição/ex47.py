flag = True

while flag:
    try:
        n = int(input("Digite um valor positivo: "))
        if n > 0:
            flag = False
        else:
            print("ERRO! O valor deve ser positivo.")
    except ValueError:
        print("ERRO! Digite apenas números inteiros.")

contador = 1
while contador <= n:
    print(contador, end=" ")
    contador += 1
