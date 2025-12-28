DISTRIBUIDOR = 0.28
IMPOSTO = 0.45

custo_carro = float(input("Insira o custo de fábrica do carro: "))
valor_distribuidor = custo_carro * DISTRIBUIDOR
valor_imposto = custo_carro * IMPOSTO
valor_total = custo_carro + valor_distribuidor + valor_imposto

print(f"O valor total do carro após os impostos é de: R${valor_total:.2f} ")
print(f"O valor total do imposto é de: R${valor_imposto:.2f}")
print(f"O valor total do distribuidor é de: R${valor_distribuidor:.2f}")
