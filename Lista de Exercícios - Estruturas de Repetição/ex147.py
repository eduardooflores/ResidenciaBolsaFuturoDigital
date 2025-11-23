try:
    valor_carro = float(input("Digite o valor do carro: R$"))

    # tabela de parcelas e percentuais de acréscimo
    opcoes = {
        6: 0.03,
        12: 0.06,
        18: 0.09,
        24: 0.12,
        36: 0.18,
        48: 0.24,
        60: 0.30
    }

    print("\n--- TABELA DE PAGAMENTO ---")

    preco_vista = valor_carro * 0.80
    print(f"À vista: Preço final = R${preco_vista:.2f}")

    for parcelas, acrescimo in opcoes.items():
        preco_final = valor_carro * (1 + acrescimo)
        valor_parcela = preco_final / parcelas
        print(f"{parcelas} parcelas: Preço final = R${preco_final:.2f} | "
              f"Valor da parcela = R${valor_parcela:.2f}")

except ValueError:
    print("ERRO! Digite um valor numérico válido para o carro.")
