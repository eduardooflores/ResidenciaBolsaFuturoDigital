soma_1_10 = 0
cont_1_10 = 0

soma_11_20 = 0
cont_11_20 = 0

soma_21_30 = 0
cont_21_30 = 0

soma_maior_30 = 0
cont_maior_30 = 0

for i in range(1, 21):
    try:
        idade = int(input(f"Digite a idade da {i}ª pessoa: "))
        peso = float(input(f"Digite o peso da {i}ª pessoa: "))

        if 1 <= idade <= 10:
            soma_1_10 += peso
            cont_1_10 += 1
        elif 11 <= idade <= 20:
            soma_11_20 += peso
            cont_11_20 += 1
        elif 21 <= idade <= 30:
            soma_21_30 += peso
            cont_21_30 += 1
        elif idade > 30:
            soma_maior_30 += peso
            cont_maior_30 += 1
        else:
            print("Idade inválida (menor que 1). Não será considerada.")

    except ValueError:
        print("ERRO! Digite valores numéricos válidos.")
        i -= 1

media_1_10 = soma_1_10 / cont_1_10 if cont_1_10 > 0 else 0
media_11_20 = soma_11_20 / cont_11_20 if cont_11_20 > 0 else 0
media_21_30 = soma_21_30 / cont_21_30 if cont_21_30 > 0 else 0
media_maior_30 = soma_maior_30 / cont_maior_30 if cont_maior_30 > 0 else 0

print("\n--- MÉDIAS DE PESO POR FAIXA ETÁRIA ---")
print(f"1 a 10 anos: {media_1_10:.2f} kg")
print(f"11 a 20 anos: {media_11_20:.2f} kg")
print(f"21 a 30 anos: {media_21_30:.2f} kg")
print(f"Maiores de 30 anos: {media_maior_30:.2f} kg")
