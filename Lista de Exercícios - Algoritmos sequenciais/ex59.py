# Qu estão 59. Uma loja vende bicicletas com um acréscimo de 50% sobre o seu preço de custo. Ela
# paga a cada vendedor 2 salários mínimos mensais, mais uma comissão de 15% sobre o preço de
# custo de cada bicicleta vendida, dividida igualmente entre eles. Escreva um algoritmo que leia o
# número de empregados da loja, o valor do salário mínimo, o preço de custo de cada bicicleta, o
# número de bicicletas vendidas, calcule e escreva: O salário final de cada empregado e o lucro (líquido)
# da loja.
# [Exemplo de dados de entrada]
# 4 (quantidade de empregados da loja) 300 (valor do salário mínimo) 150 (preço de custo de cada bicicleta)
# 200 (quantidade de bicicletas vendidas)
# [Saída para os dados de entrada acima]
# 1725 (salário final de cada empregado) 8100 (lucro da loja)

# ENTRADA
ACRESCIMO = 0.50
COMISSAO = 0.15

numero_empregados = int(input("Digite o número de empregados da loja: "))
salario_minimo = float(input("Digite o valor do salário mínimo: "))
preco_custo_bicicleta = float(input("Digite o preço de custo de cada bicicleta: "))
numero_bicicletas_vendidas = int(input("Digite o número de bicicletas vendidas: "))

# PROCESSAMENTO

# Preço de venda da bicicleta (com 50% de acréscimo)
preco_venda_bicicleta = preco_custo_bicicleta * (1 + ACRESCIMO)

# Receita total da loja
venda_total_bicicletas = preco_venda_bicicleta * numero_bicicletas_vendidas

# Comissão total (15% sobre o preço de custo * quantidade de bicicletas)
comissao_total = preco_custo_bicicleta * COMISSAO * numero_bicicletas_vendidas

# Comissão por vendedor
comissao_por_vendedor = comissao_total / numero_empregados

# Salário final de cada vendedor
salario_final = (salario_minimo * 2) + comissao_por_vendedor

# Custo total da loja (compra das bicicletas + salários + comissões)
custo_total = (preco_custo_bicicleta * numero_bicicletas_vendidas) + (salario_final * numero_empregados)

# Lucro líquido da loja
lucro_liquido = venda_total_bicicletas - custo_total

# SAÍDA
print(f"{salario_final:.0f} (salário final de cada empregado)")
print(f"{lucro_liquido:.0f} (lucro líquido da loja)")