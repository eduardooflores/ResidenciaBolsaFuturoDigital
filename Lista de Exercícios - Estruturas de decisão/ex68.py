# Questão 68. Para participar da categoria OURO do 1o. Campeonato Mundial de bolinha de Gude
# o jogador deve pesar entre 70 Kg (inclusive) e 80 Kg (inclusive) e medir de 1,75 m (inclusive) a 1,90
# m (inclusive). Faça um programa para ler a altura e o peso de um jogador e determine se o jogador
# está apto a participar do campeonato escrevendo uma das seguintes mensagens conforme cada
# situação.
# • RECUSADO POR ALTURA - se somente a altura do jogador for inválida;
# • RECUSADO POR PESO - se somente o peso do jogador for inválido;
# • TOTALMENTE RECUSADO - se a altura e o peso do jogador forem inválidos;
# • ACEITO - se a altura e o peso do jogador estiverem dentro da faixa especificada.

# ENTRADA
altura = float(input("Digite a altura do atleta em metros (ex: 1.75): "))
peso = float(input("Digite o peso do atleta em kg: "))

# PROCESSAMENTO
altura_valida = altura >= 1.75 and altura <= 1.90
peso_valido = peso >= 70 and peso <= 80

if altura_valida and peso_valido:
    print("ACEITO")
elif not altura_valida and peso_valido:
    print("RECUSADO POR ALTURA")
elif altura_valida and not peso_valido:
    print("RECUSADO POR PESO")
else:
    print("TOTALMENTE RECUSADO")