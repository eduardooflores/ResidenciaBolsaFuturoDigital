print("JOGO DE PEDRA PAPEL TESOURA: ")

nome_jogador_01 = input("Insira o nome do primeiro jogador: ")
simbolo_jogador_01 = input("Insira o símbolo (1 - Pedra, 2 - Tesoura, 3 - Papel): ").upper()
nome_jogador_02 = input("Insira o nome do segundo jogador: ")
simbolo_jogador_02 = input("Insira o símbolo (1 - Pedra, 2 - Tesoura, 3 - Papel): ").upper()

if simbolo_jogador_01 == simbolo_jogador_02:
    print("EMPATE")
elif simbolo_jogador_01 == "1" and simbolo_jogador_02 == "2":
    print(f"{nome_jogador_01} VENCEU!")
elif simbolo_jogador_01 == "1" and simbolo_jogador_02 == "3":
    print(f"{nome_jogador_02} VENCEU!")
elif simbolo_jogador_01 == "3" and simbolo_jogador_02 == "1":
    print(f"{nome_jogador_01} VENCEU!")
elif simbolo_jogador_01 == "3" and simbolo_jogador_02 == "2":
    print(f"{nome_jogador_02} VENCEU!")
elif simbolo_jogador_01 == "2" and simbolo_jogador_02 == "3":
    print(f"{nome_jogador_01} VENCEU!")
elif simbolo_jogador_01 == "2" and simbolo_jogador_02 == "1":
    print(f"{nome_jogador_02} VENCEU!")
else:
    print("Você digitar (1 - Pedra, 2 - Tesoura, 3 - Papel)")