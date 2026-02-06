tempo = int(input("Digite o tempo em anos que os fundos ficaram depositados: "))

if tempo >= 5:
    taxa = 0.95
elif tempo >= 4:
    taxa = 0.90
elif tempo >= 3:
    taxa = 0.85
elif tempo >= 2:
    taxa = 0.75
elif tempo >= 1:
    taxa = 0.65
else:
    taxa = 0.0

print(f"A taxa de juros correspondente é {taxa:.2f}% ao ano.")
