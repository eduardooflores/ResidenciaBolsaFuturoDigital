valor = float(input("Digite um valor: "))

centavos = int(round(valor * 100))

denominacoes = [
    ("nota de R$ 200", 20000),
    ("nota de R$ 100", 10000),
    ("nota de R$ 50", 5000),
    ("nota de R$ 20", 2000),
    ("nota de R$ 10", 1000),
    ("nota de R$ 5", 500),
    ("nota de R$ 2", 200),
    ("moeda de R$ 1", 100),
    ("moeda de 50 centavos", 50),
    ("moeda de 25 centavos", 25),
    ("moeda de 10 centavos", 10),
    ("moeda de 5 centavos", 5),
    ("moeda de 1 centavo", 1),
]

resultado = []

for nome, valor_denominacao in denominacoes:
    quantidade = centavos // valor_denominacao
    if quantidade > 0:
        resultado.append(f"{quantidade} {nome}{'s' if quantidade > 1 else ''}")
        centavos %= valor_denominacao

print(f"Para R$ {valor:.2f}, a menor combinação é:")
for item in resultado:
    print(item)
