EURO = 6.34
LIBRA = 7.28
DOLAR = 5.40

moeda = input("Digite a moeda que deseja converter (e - euro, l - libra, d - dolar): ").lower()
quantidade = float(input("Digite o valor em reais (R$): "))

if moeda == "e":
    total = quantidade / EURO
    print(f"R${quantidade:.2f} reais convertidos para euros dão um total de: €{total:.2f} euros.")
elif moeda == "l":
    total = quantidade / LIBRA
    print(f"R${quantidade:.2f} reais convertidos para libras dão um total de: £{total:.2f} libras.")
elif moeda == "d":
    total = quantidade / DOLAR
    print(f"R${quantidade:.2f} reais convertidos para dólares dão um total de: ${total:.2f} dólares.")
else:
    print("Moeda inválida. Escolha entre 'e' (euro), 'l' (libra) ou 'd' (dólar).")
