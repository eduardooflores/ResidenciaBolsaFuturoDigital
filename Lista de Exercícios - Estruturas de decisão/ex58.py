gols_inter = int(input("Digite o número de gols marcado pelo Inter: "))
gols_gremio = int(input("Digite o número de gols marcado pelo Grêmio: "))

if gols_inter > gols_gremio:
    print(f"O vencedor do Grenal é o INTER! Placar: {gols_inter} x {gols_gremio}")
elif gols_gremio > gols_inter:
    print(f"O vencedor do Grenal é o GRÊMIO! Placar: {gols_gremio} x {gols_inter}")
else:
    print(f"Partida empatada. Placar: {gols_inter} x {gols_gremio}")
