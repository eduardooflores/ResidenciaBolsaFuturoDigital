p1 = input("Telefonou para a vítima?").upper()
p2 = input("Esteve no local do crime?").upper()
p3 = input("Moro perto da vítima?").upper()
p4 = input("Devia para vítima?").upper()
p5 = input("Já trabalhou com a vítima?").upper()

classificacao_sim = []

if p1 == "SIM":
    classificacao_sim.append(p1)
else:
    print("Erro no dado P1. Digite SIM ou NAO.")

if p2 == "SIM":
    classificacao_sim.append(p1)
else:
    print("Erro no dado P2. Digite SIM ou NAO.")

if p3 == "SIM":
    classificacao_sim.append(p1)
else:
    print("Erro no dado P3. Digite SIM ou NAO.")

if p4 == "SIM":
    classificacao_sim.append(p1)
else:
    print("Erro no dado P4. Digite SIM ou NAO.")

if p5 == "SIM":
    classificacao_sim.append(p1)
else:
    print("Erro no dado P5. Digite SIM ou NAO.")

if len(classificacao_sim) == 2:
    print("Suspeita")
elif len(classificacao_sim) >= 3 and len(classificacao_sim) <= 4:
    print("Cúmplice")
elif len(classificacao_sim) == 5:
    print("Assasino")
elif len(classificacao_sim) == 1 or len(classificacao_sim) == 0:
    print("Inocente")