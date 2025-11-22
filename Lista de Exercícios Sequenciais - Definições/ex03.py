# ENTRADA
nome_time = input("Digite o nome do time de futebol: ").title()
nome_upper = nome_time.upper()
nome_sem_espaco = nome_time.replace(" ", "")

# PROCESSAMENTO
verifica_fc = ("FC" in nome_upper)
inicia_com_s = nome_upper[0:1] == "S"
termina_com_ense = nome_upper[-4:] == "ENSE"
verifica_clube = ("CLUBE" in nome_upper)
verifica_atletico = (("ATLETICO" in nome_upper) or ("ATLÉTICO" in nome_upper))
nome_curto = len(nome_sem_espaco) < 10
nome_valido = all(c.isalpha() or c == " " for c in nome_time)
verifica_destaque = (
    ("FC" in nome_upper) or
    ("CLUBE" in nome_upper) or
    ("GRÊMIO" in nome_upper) or
    ("GREMIO" in nome_upper)
) and not nome_curto

# SAÍDA
print(f"NOME_NORMALIZADO: {nome_time}")
print(f"TEM_FC: {verifica_fc}")
print(f"COMECA_COM_S: {inicia_com_s}")
print(f"TERMINA_COM_ENSE: {termina_com_ense}")
print(f"TEM_CLUBE: {verifica_clube}")
print(f"TEM_ATLETICO: {verifica_atletico}")
print(f"NOME_CURTO: {nome_curto}")
print(f"NOME_VALIDO: {nome_valido}")
print(f"DESTAQUE: {verifica_destaque}")