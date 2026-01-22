mes = int(input("Insira um mês Ex(1, 10): "))

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

if 1 <= mes <= 12:
    print(meses[mes - 1])
else:
    print("Mês inválido!")