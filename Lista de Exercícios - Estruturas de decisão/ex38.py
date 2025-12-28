globo = 0
sbt = 0
band = 0

for i in range(5):
    canal = input("Qual canal de TV você assiste ? (1 - Globo, 2 - SBT, 3 - Band): ")
    if canal == "1":
        globo += 1
    elif canal == "2":
        sbt += 1
    elif canal == "3":
        band += 1
    else:
        print("Você deve digitar 1 - Globo, 2 - SBT ou 3 - Band")

if globo > sbt and globo > band:
    print("O canal de TV mais assistido é a Globo!")
elif sbt > globo and sbt > band:
    print("O canal de TV mais assistido é o SBT!")
elif band > globo and band > sbt:
    print("O canal de TV mais assistido é a Band!")
else:
    print("Existem dois ou mais canais de TV que são igualmente assistidos!")