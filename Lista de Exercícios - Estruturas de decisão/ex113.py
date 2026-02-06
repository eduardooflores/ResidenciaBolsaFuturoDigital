salario = float(input("Digite seu salário: "))
valor_gasto_cesta_basico = float(input("Digite o valor gasto na cesta básica: "))
porcentagem_salario_cesta = (valor_gasto_cesta_basico / salario) * 100

if porcentagem_salario_cesta <= 25:
    print("Esbanjador")
    print(f"Você gasta {porcentagem_salario_cesta:.2f}% do seu salário na cesta básica.")
elif porcentagem_salario_cesta <= 53:
    print("Gastador")
    print(f"Você gasta {porcentagem_salario_cesta:.2f}% do seu salário na cesta básica.")
elif porcentagem_salario_cesta <= 75:
    print("Comedido")
    print(f"Você gasta {porcentagem_salario_cesta:.2f}% do seu salário na cesta básica.")
else:
    print("Essencial")
    print(f"Você gasta {porcentagem_salario_cesta:.2f}% do seu salário na cesta básica.")