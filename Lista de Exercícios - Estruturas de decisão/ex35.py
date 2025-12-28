GORJETA = 0.10

bebidas = float(input("Informe o valor gasto com bebidas: "))
comidas = float(input("Informe o valor gasto com comidas: "))

valor_total = bebidas + comidas
valor_gorjeta = valor_total * GORJETA
valor_total_gorjeta = valor_total + valor_gorjeta

print(f"O valor total sem a gorjeta do garçom é de: R${valor_total:.2f}")
print(f"O valor total com a gorjeta do garçom é de: R${valor_total_gorjeta:.2f}")