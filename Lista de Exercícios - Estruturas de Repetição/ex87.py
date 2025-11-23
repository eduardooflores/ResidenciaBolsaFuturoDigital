flag = True
lista_numeros = []

while flag:
    try:
        numero = int(input("Digite valores (para terminar digite um valor negativo): "))
        if numero < 0:
            flag = False
        else:
            lista_numeros.append(numero)
    except:
        print("ERRO! DADOS INVÁLIDOS")

# Inicializa variáveis
soma_pares = 0
soma_impar = 0
total_impar = 0
contador_maior_50 = 0
contador_maior_20 = 0
soma_intervalo = 0
total_intervalo = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        soma_pares += numero
        if 50 <= numero <= 150:
            soma_intervalo += numero
            total_intervalo += 1
    else:
        soma_impar += numero
        total_impar += 1

    if numero > 50:
        contador_maior_50 += 1
    if numero > 20:
        contador_maior_20 += 1

# Resultados
maior_valor = max(lista_numeros) if lista_numeros else 0
menor_valor = min(lista_numeros) if lista_numeros else 0
media_impar = soma_impar / total_impar if total_impar > 0 else 0
percentagem = (contador_maior_20 / len(lista_numeros)) * 100 if lista_numeros else 0
media_intervalo = soma_intervalo / total_intervalo if total_intervalo > 0 else 0
total_valores = len(lista_numeros)

# Saída
print(f"a) Maior valor: {maior_valor}")
print(f"b) Menor valor: {menor_valor}")
print(f"c) Soma dos valores pares: {soma_pares}")
print(f"d) Média dos valores ímpares: {media_impar:.2f}")
print(f"e) Quantos números maiores que 50: {contador_maior_50}")
print(f"f) Percentagem de valores maiores que 20: {percentagem:.2f}%")
print(f"g) Média dos pares entre 50 e 150: {media_intervalo:.2f}")
print(f"h) Total de valores digitados: {total_valores}")
