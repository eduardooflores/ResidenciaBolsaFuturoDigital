# Qu estão 19. Elabore um algoritmo que lê 4 valores inteiros e mostra: a soma dos valores; a
# subtração do 1o valor e o 2o valor; a multiplicação dos 3 primeiros valores digitados;a média dos
# valores; o resultado da equação (1o valor + 2o valor) / (3o valor – 4o valor).

# ENTRADA
primeiro_valor = 5
segundo_valor = 10
terceiro_valor = 20
quarto_valor = 30

# PROCESSAMENTO
soma = primeiro_valor + segundo_valor + terceiro_valor + quarto_valor
subtracao = primeiro_valor - segundo_valor
multiplicacao = primeiro_valor * segundo_valor * terceiro_valor
media = (primeiro_valor + segundo_valor + terceiro_valor + quarto_valor) / 4
equacao = (primeiro_valor + segundo_valor) / (terceiro_valor - quarto_valor)

# SAÍDA
print(f"A soma de todos os valores é de: {soma}")
print(f"A subtração do primero valor com o segundo é de: {subtracao}")
print(f"A multiplicação dos três primeiros valores é de: {soma}")
print(f"O valor da equação é de: {soma}")