# Questão 110 - Divisores de 1 a 20

for n in range(1, 21):
    divisores = []
    for d in range(1, n + 1):
        if n % d == 0:
            divisores.append(d)

    print(f"{n}: {' '.join(map(str, divisores))}")
