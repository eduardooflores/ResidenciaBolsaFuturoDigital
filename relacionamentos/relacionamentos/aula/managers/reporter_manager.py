from datetime import date
from django.db.models import QuerySet
from django.db.models.aggregates import Count

from .base_manager import BaseManager


class ReporterManager(BaseManager):

    def find_by_nome(self, nome: str) -> list['Reporter']:
        if isinstance(nome, str) and len(nome) > 0:
            consulta = self.filter(name__icontains=nome).order_by('-name')[:2]
            return list(consulta)
        else:
            raise TypeError('O nome deve ser string e não pode estar vazia')

    def find_by_publication_date_since(self, publication_date: date) -> QuerySet['Reporter']:
        if isinstance(publication_date, date):
            today = date.today()
            consulta = self.filter(article__pub_date__range=(publication_date, today))
            return consulta
        else:
            raise TypeError("Você deve consultar com um objeto date")

    def find_prova(self) -> QuerySet['Reporter']:
        todos = self.filter()
        lista_eventos_fora = []

        for x in todos:
            for exemplo in x.exemplo_set.all():
                if x.cpf == exemplo.person.cpf:
                    lista_eventos_fora.append(x.id)

        todos = todos.exclude(id__in=lista_eventos_fora)

        return todos

    def find_email(self, email: str) -> QuerySet['Reporter']:
        if isinstance(email, str) and len(email) > 0:
            consulta = self.filter(email__contains=email)
            return consulta
        else:
            raise TypeError('O nome deve ser string e não pode estar vazia')

    def count_papers_reporter(self, name: str) -> list[tuple[str, str]]:
        if isinstance(name, str) and len(name):
            consulta = self.filter(name__icontains=name).annotate(Count('paper'))
            lista = []
            for resultado in consulta:
                if resultado.paper__count == 0:
                    lista.append((resultado.name, "Não trabalha direito"))
                else:
                    lista.append((resultado.name, str(resultado.paper__count)))
            return lista

    def last_three_digits_cpf(self, cpf: str):
        if not isinstance(cpf, str) or len(cpf) != 3:
            raise ValueError("Você deve digitar exatamente os três últimos dígitos do CPF")

        consulta = self.filter(cpf__endswith=cpf).values("name", "cpf")
        return consulta

    def count_reporter(self):
        consulta = self.count()
        return consulta


