soma = 0

for numero in range(50, 151):
    if numero % 2 == 0:
        soma += numero

print(f"A soma dos números pares entre 50 e 150 é: {soma}")
