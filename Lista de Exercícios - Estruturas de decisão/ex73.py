quantidade_livros = int(input("Digite a quantidade de livros que deseja comprar: "))

valor_livro_criterio_a = 0.25
valor_livro_criterio_b = 0.50

valor_livros_criterio_a = quantidade_livros * valor_livro_criterio_a
valor_livros_criterio_b = quantidade_livros * valor_livro_criterio_b

total_criterio_a = valor_livros_criterio_a + 7.50
total_criterio_b = valor_livros_criterio_b + 2.50

if total_criterio_a < total_criterio_b:
    print(f"A melhor opção para pagar o menor preço é utilizar o Critério A. O total fica em: R${total_criterio_a:.2f}")
elif total_criterio_b < total_criterio_a:
    print(f"A melhor opção para pagar o menor preço é utilizar o Critério B. O total fica em: R${total_criterio_b:.2f}")
else:
    print(f"Os dois critérios são igualmente vantajosos. O total fica em: {total_criterio_a:.2f}")