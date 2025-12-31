print("CALCULADORA")
n1 = float(input("Digite o primeiro número da operação: "))
n2 = float (input("Digite o segundo número da operação: "))
operador = input("Digite o operador (+, -, *, /): ")

if operador == "+":
    total = n1 + n2
    print(f"O total da operação usando o operador + é: {total:.2f}")
elif operador == "-":
    total = n1 - n2
    print(f"O total da operação usando o operador - é: {total:.2f}")
elif operador == "*":
    total = n1 * n2
    print(f"O total da operação usando o operador * é: {total:.2f}")
elif operador == "/":
    total = n1 / n2
    print(f"O total da operação usando o operador / é: {total:.2f}")
else:
    print("Operação inválida!")