verbo = input("Digite um verbo no infinitivo: ").lower()

if verbo[-2:] != "ar" and verbo[-2:] != "er" and verbo[-2:] != "ir":
    print("Verbo não está no infinitivo")
elif verbo[-2:] == "ar":
    print("Verbo da 1a. Conjugação")
elif verbo[-2:] == "er":
    print("Verbo da 2a. Conjugação")
elif verbo[-2:] == "ir":
    print("Verbo da 3a. Conjugação")