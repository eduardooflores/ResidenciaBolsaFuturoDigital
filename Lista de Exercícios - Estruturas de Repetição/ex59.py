try:
    qntd_valor = int(input("Digite a quantidade de valores que deseja informar: "))
except ValueError:
    print("ERRO! Digite um valor inteiro!")
    qntd_valor = 0

if qntd_valor > 0:
    for i in range(qntd_valor):
        flag = True
        while flag:
            try:
                valor = float(input(f"Digite o {i+1}º valor: "))
                raiz_cubica = valor ** (1 / 3)
                print(f"A raiz cúbica de {valor} é: {raiz_cubica:.2f}")  # saída formatada
                flag = False
            except ValueError:
                print("ERRO! Digite um número válido para calcular a raiz cúbica.")
else:
    print("Nenhum valor informado para cálculo.")
