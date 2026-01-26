from django.db.models import QuerySet

from digital.managers.base import BaseManager


class AlunoManager(BaseManager):

    def find_by_name(self, nome: str) -> QuerySet['Aluno']:
        if isinstance(nome, str) and len(nome) > 0:
            query = self.filter(nome__icontains=nome).order_by("nome")
            return query
        else:
            raise TypeError("Nome deve ser uma string")

    def find_by_matricula(self, matricula: str) -> QuerySet['Aluno']:
        if isinstance(matricula, str) and len(matricula) > 0:
            query = self.filter(matricula__iexact=matricula)
            return query
        else:
            raise TypeError("Matricula deve ser uma string")

    def find_by_name_and_matricula(self, nome: str, matricula: str) -> QuerySet['Aluno']:
        if not all([isinstance(x, str) for x in (nome, matricula)]):
            raise TypeError("Nome e matrícula devem ser strings")
        else:
            query = self.filter(nome__iexact=nome, matricula__iexact=matricula)
            return query