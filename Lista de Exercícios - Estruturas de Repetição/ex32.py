try:
    tabuada = int(input("Digite o número para calcular a tabuada: "))
    if tabuada < 0:
        print("A tabuada deve ser maior ou igual a zero.")
    else:
        for multiplicador in range(1, 11):
            total = tabuada * multiplicador
            print(f"{multiplicador} x {tabuada} = {total}")
except ValueError:
    print("ERRO! Deve ser digtado um número inteiro.")