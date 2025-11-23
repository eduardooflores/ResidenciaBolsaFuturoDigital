flag = True

grenais = 0
vitorias_inter = 0
vitorias_gremio = 0
empates = 0

while flag:
    try:
        gols_inter = int(input("Digite o número de gols marcado pelo inter: "))
        gols_gremio = int(input("Digite o número de gols marcado pelo grêmio: "))

        if gols_inter > gols_gremio:
            vitorias_inter += 1
            print("INTER VENCEU!")
        elif gols_gremio > gols_inter:
            vitorias_gremio += 1
            print("GRÊMIO VENCEU!")
        else:
            empates += 1
            print("EMPATE")

        grenais += 1

        flag_op = True
        while flag_op:
            try:
                op = int(input("Novo GRENAL 1.Sim 2.Não?"))
                if op == 1:
                    flag_op = False
                elif op == 2:
                    flag_op = False
                    flag = False
                else:
                    print("DADOS INVÁLIDOS! DIGITE 1 para cadastrar novo grenal ou 2 para sair.")
            except:
                print("ERRO! DADOS INVÁLIDOS DIGITE 1 OU 2")

    except ValueError:
        print("Os dados deve numéricos!")

if vitorias_inter > vitorias_gremio:
    maior_vencedor = "INTER"
elif vitorias_gremio > vitorias_inter:
    maior_vencedor = "GRÊMIO"
else:
    maior_vencedor = "SEM VENCEDOR"

print(f"Número de GRENAIS analisados: {grenais}")
print(f"O número de vitórias do INTER: {vitorias_inter}")
print(f"O número de vitórias do GRÊMIO: {vitorias_gremio}")
print(f"O número de empates: {empates}")
print(f"Time que mais venceu: {maior_vencedor}")