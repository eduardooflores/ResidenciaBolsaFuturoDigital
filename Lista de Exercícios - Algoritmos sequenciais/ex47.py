# ENTRADA
TAMANHO_LATA = 350
TAMANHO_GARRAFA = 600
TAMANHO_GARRAFA_2L = 2000

qntd_latas = int(input("Digite a quantidade de latas compradas: "))
qntd_garrafa = int(input("Digite a quantidade de garrafas compradas: "))
qntd_garrafas_2l = int(input("Digite a quantidade de garrafas 2L compradas: "))

# PROCESSAMENTO
total_litros_latas = qntd_latas * TAMANHO_LATA
total_litros_garrafas = qntd_garrafa * TAMANHO_GARRAFA
total_litros_garrafas_2l = qntd_garrafas_2l * TAMANHO_GARRAFA_2L
total_litros = (total_litros_latas + total_litros_garrafas + total_litros_garrafas_2l) / 1000

# SAÍDA
print(f"O total de litros comprados foi de: {total_litros:.2f}")