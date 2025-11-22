#  Questão 64. O custo ao consumidor de um carro novo é a soma do custo de fábrica com a
# percentagem do distribuidor e dos impostos (aplicados, primeiro os impostos sobre o custo de
# fábrica, e depois a percentagem do distribuidor sobre o resultado). Supondo que a percentagem do
# distribuidor seja de 28% e os impostos 45%. Escrever um algoritmo que leia o custo de fábrica de
# um carro e informe o custo ao consumidor do mesmo.

# ENTRADA
custo_fabrica_carro = float(input("Digite o custo de fábrica do carro: "))

# PROCESSAMENTO
# Primeiro aplicar os impostos
valor_com_imposto = custo_fabrica_carro * (1 + IMPOSTOS)

# Depois aplicar a margem do distribuidor
custo_ao_consumidor = valor_com_imposto * (1 + PORCENTAGEM_DISTRIBUIDOR)

# SAÍDA
print(f"O custo ao consumidor é: R$ {custo_ao_consumidor:.2f}")