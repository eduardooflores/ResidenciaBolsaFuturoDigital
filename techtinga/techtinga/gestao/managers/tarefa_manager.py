from django.db.models import QuerySet

from .base_manager import BaseManager
from gestao.models import Projeto


class TarefaManager(BaseManager):

    def listar_tarefas_projeto(self, projeto: Projeto) -> QuerySet['Tarefa']:
        if not isinstance(projeto, Projeto):
            raise ValidationError("O parâmetro deve ser uma instância de Projeto.")

        consulta = self.filter(projeto=projeto).order_by("responsavel", "status", "criacao")
        return consulta

    def listar_tarefas_colaborador(self, responsavel: str) -> QuerySet['Tarefa']:
        if not responsavel or not isinstance(responsavel, str):
            raise ValidationError("O responsável deve ser informado como uma string.")

        consulta = self.filter(responsavel=responsavel).order_by("status", "criacao")
        return consulta