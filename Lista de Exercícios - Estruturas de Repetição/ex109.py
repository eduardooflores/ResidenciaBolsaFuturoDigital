notas = [100, 50, 20, 10, 5, 2, 1]
moedas = [50, 25, 10, 5, 1]

valor = float(input("Digite um valor em reais: "))

parte_inteira = int(valor)
parte_centavos = round((valor - parte_inteira) * 100)

print(f"Valor: R${valor:.2f}")

for nota in notas:
    qtd = parte_inteira // nota
    if qtd > 0:
        print(f"{qtd} nota(s) de R${nota}")
        parte_inteira %= nota

for moeda in moedas:
    qtd = parte_centavos // moeda
    if qtd > 0:
        print(f"{qtd} moeda(s) de {moeda} centavos")
        parte_centavos %= moeda
