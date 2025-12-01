tamanho_metros_quadrados = float(input("Digite o tamanho a ser pintado em m²: "))

COBERTURA_TINTA = 3
TAMANHO_LATA_TINTA = 18
PRECO = 80

qntd_litros_necessarios = tamanho_metros_quadrados / COBERTURA_TINTA
qntd_latas_necessarias = (qntd_litros_necessarios + TAMANHO_LATA_TINTA - 1) // TAMANHO_LATA_TINTA
preco_total = qntd_latas_necessarias * PRECO

print("Quantidade de latas:", int(qntd_latas_necessarias))
print("Preço total: R$", int(preco_total))




