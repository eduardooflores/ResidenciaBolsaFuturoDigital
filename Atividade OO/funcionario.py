from datetime import date


class Funcionario:
    def __init__(self, nome: str, nascimento: date, cargo: str,
                 departamento: str, admissao: date,
                 regime_trabalho: int, valor_hora: float):

        if not (2 <= len(nome) <= 50):
            raise ValueError("Nome deve ter entre 2 e 50 caracteres.")
        if (date.today().year - nascimento.year) < 16:
            raise ValueError("Funcionário deve ter pelo menos 16 anos.")
        if not (3 <= len(cargo) <= 30):
            raise ValueError("Cargo deve ter entre 3 e 30 caracteres.")
        if departamento and not (5 <= len(departamento) <= 20):
            raise ValueError("Departamento deve ter entre 5 e 20 caracteres.")
        if admissao > date.today():
            raise ValueError("Data de admissão não pode ser futura.")
        if not (10 <= regime_trabalho <= 60):
            raise ValueError("Regime de trabalho deve estar entre 10 e 60 horas semanais.")
        if valor_hora < 0.01:
            raise ValueError("Valor da hora deve ser maior que 0.01.")

        self.nome = nome
        self.nascimento = nascimento
        self.cargo = cargo
        self.departamento = departamento
        self.admissao = admissao
        self.regime_trabalho = regime_trabalho
        self.valor_hora = valor_hora

    def __str__(self):
        return (f"Nome: {self.nome}, Nascimento: {self.nascimento}, Cargo: {self.cargo}, "
                f"Departamento: {self.departamento}, Admissão: {self.admissao}, "
                f"Regime: {self.regime_trabalho}h/semana, Valor Hora: R${self.valor_hora:.2f}")

    def parabenizar_funcionario(self):
        hoje = date.today()
        if hoje.day == self.nascimento.day and hoje.month == self.nascimento.month:
            return f"Parabéns {self.nome}, feliz aniversário!"
        else:
            return f"Hoje não é aniversário de {self.nome}."

    def calcular_salario(self, mes: int):
        horas_mes = self.regime_trabalho * 4
        salario_bruto = horas_mes * self.valor_hora

        desconto_inss = salario_bruto * 0.08
        desconto_sindicato = salario_bruto * 0.01

        desconto_ir = 0
        if salario_bruto <= 5000:
            desconto_ir = 0
        elif salario_bruto <= 7000:
            desconto_ir = salario_bruto * 0.125
        elif salario_bruto <= 50000:
            desconto_ir = salario_bruto * 0.275
        else:
            desconto_ir = salario_bruto * (0.275 + 0.10)

        salario_liquido = salario_bruto - (desconto_inss + desconto_sindicato + desconto_ir)
        return salario_liquido