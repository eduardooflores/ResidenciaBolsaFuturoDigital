# Qu estão 14. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
# metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3
# metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao
# usuário a quantidades de latas de tinta a serem compradas e o preço total.

tamanho_metros_quadrados = float(input("Digite o tamanho a ser pintado em m²: "))

COBERTURA_TINTA = 3
TAMANHO_LATA_TINTA = 18
PRECO = 80

qntd_litros_necessarios = tamanho_metros_quadrados / COBERTURA_TINTA
qntd_latas_necessarias = (qntd_litros_necessarios + TAMANHO_LATA_TINTA - 1) // TAMANHO_LATA_TINTA
preco_total = qntd_latas_necessarias * PRECO

print("Quantidade de latas:", int(qntd_latas_necessarias))
print("Preço total: R$", int(preco_total))




