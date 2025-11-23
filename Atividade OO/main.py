from datetime import date
from funcionario import Funcionario

if __name__ == "__main__":
    f1 = Funcionario("Ana", date(2000, 11, 23), "Analista", "Tecnologia", date(2020, 5, 10), 40, 30)
    f2 = Funcionario("Bruno", date(1995, 6, 15), "Engenheiro", "Projetos", date(2018, 3, 20), 40, 45)
    f3 = Funcionario("Carla", date(1988, 11, 23), "Gerente", "Recursos Humanos", date(2010, 1, 5), 40, 100)
    f4 = Funcionario("Daniel", date(1975, 8, 10), "Diretor", "Administração", date(2000, 2, 1), 40, 400)
    f5 = Funcionario("Eva", date(2005, 11, 23), "Estagiária", "Financeiro", date(2023, 7, 1), 20, 25)

    funcionarios = [f1, f2, f3, f4, f5]

    for f in funcionarios:
        print("\n", f)
        print(f.parabenizar_funcionario())
        print(f"Salário líquido: R${f.calcular_salario(mes=11):.2f}")