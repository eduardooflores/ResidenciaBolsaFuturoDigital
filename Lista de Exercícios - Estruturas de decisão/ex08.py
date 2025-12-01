contador_par = 0
contador_impar = 0

# ENTRADA
primeiro_valor = int(input("Digite o primeiro valor: "))
segundo_valor = int(input("Digite o segundo valor: "))
terceiro_valor = int(input("Digite o terceiro valor: "))

# PROCESSAMENTO
if primeiro_valor % 2 == 0:
    contador_par += 1
else:
    contador_impar += 1

if segundo_valor % 2 == 0:
    contador_par += 1
else:
    contador_impar += 1

if terceiro_valor % 2 == 0:
    contador_par += 1
else:
    contador_impar += 1

# SAÍDA
print(f"Existem {contador_par} números PAR entre os números")
print(f"Existem {contador_impar} números ÍMPAR entre os números")