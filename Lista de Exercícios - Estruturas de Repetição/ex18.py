fim = int(input("Digite o valor final do intervalo: "))

soma_pares = 0

for num in range(1, fim + 1):
    if num % 2 == 0:
        soma_pares += num

print(f"A soma dos números pares de 1 até {fim} é: {soma_pares}")
