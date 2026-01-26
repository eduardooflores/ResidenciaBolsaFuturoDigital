from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.db.models import CASCADE

from gestao.enumerations.linguagem_programacao import LinguagemProgramacao
from gestao.enumerations.status import Status
from gestao.managers.tarefa_manager import TarefaManager
from gestao.models import Projeto
from gestao.models.base_model import BaseModel
from django.db import models


class Tarefa(BaseModel):

    titulo = models.CharField(max_length=100,
                              validators=[MinLengthValidator(5)],
                              verbose_name="Título da Tarefa",
                              help_text="Digite o título da tarefa")

    descricao = models.TextField(validators=[MinLengthValidator(0), MaxLengthValidator(1000)],
                                 null=True, blank=True,
                                 verbose_name="Descrição da Tarefa",
                                 help_text="Digite a descrição da tarefa")

    linguagem = models.CharField(max_length=12,
                                 validators=[MinLengthValidator(1)],
                                 choices=LinguagemProgramacao.choices,
                                 verbose_name="Tipo de Linguagem",
                                 help_text="Seleciona a Linguagem de Programação")

    estimativa_horas = models.IntegerField(validators=[MinValueValidator(0)],
                                           verbose_name="Estimativa de Horas para Tarefa",
                                           help_text="Digite a estimativa de horas para realizar a tarefa")

    horas_registradas = models.IntegerField(validators=[MinValueValidator(0)],
                                            verbose_name="Horas Registradas da Tarefa",
                                            help_text="Digite as horas registradas da tarefa")

    prioridade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                     verbose_name="Prioridade da Tarefa",
                                     help_text="Digite a prioridade da tarefa (1 - 5)")

    status = models.CharField(max_length=14,
                              validators=[MinLengthValidator(6)],
                              choices=Status.choices,
                              verbose_name="Status da Tarefa",
                              help_text="Selecione o Status da tarefa")

    responsavel = models.CharField(max_length=50,
                                   validators=[MinLengthValidator(3)],
                                   verbose_name="Digite o Responsável",
                                   help_text="Digite o responsável pela tarefa")

    criacao = models.DateTimeField(verbose_name="Data da Criação da Tarefa",
                                   help_text="Insira a data da criação da tarefa")

    conclusao = models.DateTimeField(null=True, blank=True,
                                     verbose_name="Data da conclusão da Tarefa",
                                     help_text="Insira a data da conclusão da tarefa")

    projeto = models.ForeignKey(Projeto,on_delete=models.CASCADE,
                                related_name="tarefas",
                                verbose_name="Projeto",
                                help_text="Selecione um projeto")

    objects = TarefaManager()

    def __str__(self):
        criacao_str = self.criacao.strftime('%d/%m/%Y') if self.criacao else "N/A"
        conclusao_str = self.conclusao.strftime('%d/%m/%Y') if self.conclusao else "N/A"
        return (f"Responsável: {self.responsavel} - Linguagem: {self.linguagem} - Título: {self.titulo} "
                f"Criação: {criacao_str} - Conclusão: {conclusao_str} " f"Estimativa: {self.estimativa_horas} horas - Status: {self.status}")

    def clean(self):
        if self.criacao and self.conclusao:
            if self.conclusao < self.criacao:
                raise ValidationError({
                    "conclusao": "A conclusão não pode ser anterior a criação do projeto."
                })

        if self.criacao and self.projeto and self.projeto.inicio:
            if self.criacao.date() < self.projeto.inicio:
                raise ValidationError({
                    "criacao": "A criação da tarefa não pode ser anterior ao início do projeto."
                })
        if self.projeto:
            if not self.projeto.ativo:
                raise ValidationError({
                    "projeto": "Não é possível criar tarefas em um projeto desativado."
                })
            if self.projeto.fim:
                raise ValidationError({
                    "projeto": "Não é possível criar tarefas em um projeto com data de finalização já informada."
                })