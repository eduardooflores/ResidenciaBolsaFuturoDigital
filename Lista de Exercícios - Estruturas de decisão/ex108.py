x = float(input("Digite o valor de x: "))

if x <= 1:
    y = 1
elif x <= 2:
    y = 2
elif x <= 3:
    y = x * x
else:
    y = x * x * x

print("y =", y)