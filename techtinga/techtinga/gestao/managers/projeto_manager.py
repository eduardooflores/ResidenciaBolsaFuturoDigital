from datetime import date

from django.db.models import QuerySet
from django.core.exceptions import ValidationError

from .base_manager import BaseManager
from ..enumerations.linguagem_programacao import LinguagemProgramacao


class ProjetoManager(BaseManager):

    def listar_projetos_linguagem(self, inicio: date, fim: date, linguagem: LinguagemProgramacao) -> QuerySet['Projeto']:
        if not isinstance(inicio, date) or not isinstance(fim, date):
            raise ValidationError("As datas devem ser objetos do tipo date.")
        if inicio > fim:
            raise ValidationError("A data inicial não pode ser maior que a final.")
        if not isinstance(linguagem, LinguagemProgramacao):
            raise ValidationError("O parâmetro linguagem deve ser uma instância de LinguagemProgramacao.")

        consulta = self.filter(tarefas__criacao__range=(inicio, fim), tarefas__linguagem=linguagem).distinct()
        return consulta