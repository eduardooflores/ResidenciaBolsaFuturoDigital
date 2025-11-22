# Questão 22. Um carro gasta 10 litros de gasolina para andar 130 km. Sabendo que o tanque do
# carro comporta 60 litros, quantos quilômetros você conseguirá andar com o carro? Faça um
# algoritmo que calcula o valor e mostra na tela.

# ENTRADA
TAMANHO_TANQUE = 60
km_po_litro = 130 / 10
distancia_total_possivel = km_po_litro * TAMANHO_TANQUE

# PROCESSAMENTO
print(f"A distância total que o carro consegue andar com o tanque cheio é de: {distancia_total_possivel}km")