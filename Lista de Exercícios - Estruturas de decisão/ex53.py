# Questão 53. Faça um algoritmo que leia o número de gols marcados pelo Grêmio e número de
# gols marcados pelo Inter em um Grenal. Mostre na tela o nome do vencedor e quantos gols o time
# vencedor fez a mais. Caso não haja vencedor, mostre na tela o total de gols de cada time com a
# mensagem: EMPATE

# ENTRADA
gols_inter = int(input("Digite o número de gols que o INTER fez: "))
gols_gremio = int(input("Digite o número de gols que o GRÊMIO fez: "))

# PROCESSAMENTO
if gols_inter > gols_gremio:
    diferenca_gols = gols_inter - gols_gremio
    print(f"O vencedor do jogo foi o INTER com um total de {diferenca_gols} gols a mais.")
elif gols_gremio > gols_inter:
    diferenca_gols = gols_gremio - gols_inter
    print(f"O vencedor do jogo foi o GRÊMIO com um total de {diferenca_gols} gols a mais.")
elif gols_inter == gols_gremio:
    print(f"O jogo EMPATOU com um total de {gols_inter} gols do INTER e {gols_gremio} gols do GRÊMIO")