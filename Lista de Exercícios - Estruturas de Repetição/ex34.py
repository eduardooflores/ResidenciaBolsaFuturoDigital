# while
i = 1 # tabuada

while i <= 5:
    print(f"Tabuada do {i}:")

    j = 1  # multiplicador
    while j <= 10:
        print(f"{i} x {j} = {i * j}")
        j += 1

    print()  # Linha em branco para separar cada tabuada
    i += 1

# for
for i in range(1, 6): # tabuada
    print(f"Tabuada do {i}:")
    for j in range(1, 11): # multiplicador
        print(f"{i} x {j} = {i * j}")
    print()  # Linha em branco para separar cada tabuada
