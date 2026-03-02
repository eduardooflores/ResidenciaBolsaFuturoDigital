try:
    tabuada = int(input("Digite o número para calcular a tabuada: "))
    if tabuada < 0:
        print("A tabuada deve ser maior ou igual a zero.")
    else:
        multiplicador = 1
        while multiplicador <= 10:
            total = tabuada * multiplicador
            print(f"{multiplicador} x {tabuada} = {total}")
            multiplicador += 1

except ValueError:
    print("ERRO! Deve ser digtado um número inteiro.")