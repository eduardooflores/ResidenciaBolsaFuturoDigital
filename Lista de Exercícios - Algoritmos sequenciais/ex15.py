# Questão 15. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em
# metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6
# metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões
# de 3,6 litros, que custam R$ 25,00.
# ◦ Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços
# em 3 situações:
# ◦ comprar apenas latas de 18 litros;
# ◦ comprar apenas galões de 3,6 litros;
# ◦ misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e
# sempre arredonde os valores para cima, isto é, considere latas cheias.

# Entrada
tamanho_metros_quadrados = float(input("Digite o tamanho da área a ser pintada em m²: "))

# Constantes
COBERTURA_TINTA = 6
TAMANHO_LATA = 18
TAMANHO_GALAO = 3.6
PRECO_LATA = 80
PRECO_GALAO = 25

# Calcular litros com 10% de folga
litros_necessarios = tamanho_metros_quadrados / COBERTURA_TINTA
litros_com_folga = litros_necessarios * 1.1

# --- 1. Apenas latas de 18L ---
qtd_latas = litros_com_folga / TAMANHO_LATA
qtd_latas_cheia = int(qtd_latas) + (qtd_latas > int(qtd_latas))
preco_latas = qtd_latas_cheia * PRECO_LATA

# --- 2. Apenas galões de 3.6L ---
qtd_galoes = litros_com_folga / TAMANHO_GALAO
qtd_galoes_cheio = int(qtd_galoes) + (qtd_galoes > int(qtd_galoes))
preco_galoes = qtd_galoes_cheio * PRECO_GALAO

# --- 3. Mistura de latas + galões para menor preço ---

# Parte inteira de latas
qtd_latas_misto = int(litros_com_folga / TAMANHO_LATA)
# Litros restantes depois das latas
litros_restantes = litros_com_folga - (qtd_latas_misto * TAMANHO_LATA)
# Quantidade de galões para o restante
qtd_galoes_misto = litros_restantes / TAMANHO_GALAO
qtd_galoes_misto_cheio = int(qtd_galoes_misto) + (qtd_galoes_misto > int(qtd_galoes_misto))
preco_misto = (qtd_latas_misto * PRECO_LATA) + (qtd_galoes_misto_cheio * PRECO_GALAO)

# Saída
print("\n--- Situação 1: Apenas latas de 18L ---")
print("Quantidade de latas:", qtd_latas_cheia)
print("Preço total: R$ {:.2f}".format(preco_latas))

print("\n--- Situação 2: Apenas galões de 3.6L ---")
print("Quantidade de galões:", qtd_galoes_cheio)
print("Preço total: R$ {:.2f}".format(preco_galoes))

print("\n--- Situação 3: Mistura de latas e galões ---")
print("Quantidade de latas:", qtd_latas_misto)
print("Quantidade de galões:", qtd_galoes_misto_cheio)
print("Preço total: R$ {:.2f}".format(preco_misto))
