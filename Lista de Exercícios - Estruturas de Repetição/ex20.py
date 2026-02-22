while True:
    try:
        valor = int(input("Informe um valor inteiro positivo: "))
        if valor > 0:
            break
        else:
            print("Por favor, digite um número maior que zero.")
    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros.")

soma_pares = 0
produto_impares = 1

for i in range(1, valor + 1):
    if i % 2 == 0:
        soma_pares += i
    else:
        produto_impares *= i

print(f"Soma dos valores pares de 1 até {valor}: {soma_pares}")
print(f"Produto dos valores ímpares de 1 até {valor}: {produto_impares}")
