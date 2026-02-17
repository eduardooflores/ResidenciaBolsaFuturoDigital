try:
    primeiro_valor = float(input("Digite o primeiro valor: "))
    segundo_valor = float(input("Digite o segundo valor: "))

    soma = primeiro_valor + segundo_valor

    print(f"A soma dos valores {primeiro_valor:.2f} + {segundo_valor:.2f} é: {soma:.2f}")

except ValueError:
    print("ERRO! O valor digitado deve ser um número.")