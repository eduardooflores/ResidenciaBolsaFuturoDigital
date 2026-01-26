from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models.fields import DateField

from gestao.enumerations.tipo_projeto import TipoProjeto
from gestao.managers.projeto_manager import ProjetoManager
from gestao.models.base_model import BaseModel
from gestao.validators import InicioProjetoValidator


class Projeto(BaseModel):

    codigo = models.CharField(max_length=20,
                              validators=[MinLengthValidator(5)],
                              unique=True,
                              verbose_name="Código do Projeto",
                              help_text="Digite o código do projeto")

    nome = models.CharField(max_length=100,
                            validators=[MinLengthValidator(5)],
                            verbose_name="Nome do Projeto",
                            help_text="Digite o nome do projeto")

    tipo_projeto = models.CharField(max_length=30,
                                    validators=[MinLengthValidator(10)],
                                    choices=TipoProjeto.choices,
                                    verbose_name="Tipo do Projeto",
                                    help_text="Selecione o tipo do projeto")

    cliente = models.CharField(max_length=50,
                               validators=[MinLengthValidator(3)],
                               verbose_name="Nome do Cliente",
                               help_text="Digite o nome do cliente")

    gerente = models.CharField(max_length=50,
                               validators=[MinLengthValidator(3)],
                               verbose_name="Nome do Gerente",
                               help_text="Digite o nome do gerente")

    inicio = models.DateField(validators=[InicioProjetoValidator()],
                       verbose_name="Data de Início do Projeto",
                       help_text="Insira a data de início do projeto")

    previsao_termino = models.DateField(verbose_name="Previsã de Finalização do Projeto",
                                        help_text="Insira a data para a previsão de finalização do projeto")

    fim = models.DateField(null=True,blank=True,
                           verbose_name="Data do Fim do Projeto",
                           help_text="Insira a data de finalização do projeto")

    orcamento = models.DecimalField(max_digits=8, decimal_places=2,
                                    verbose_name="Orçamento do Projeto",
                                    help_text="Insira o orçamento do projeto")

    ativo = models.BooleanField(default=True,
                                verbose_name="Situação do Proeto",
                                help_text="Marque se o projeto está ATIVO ou DESATIVADO")

    objects = ProjetoManager()

    def __str__(self):
        return (f"Cliente: {self.cliente} - Nome: {self.nome} - Tipo do Projeto: {self.tipo_projeto} - "
                f"Orçamento: R${self.orcamento:.2f} - Início: {self.inicio.strftime('%d/%m/%Y')} - "
                f"Previsão de Término: {self.previsao_termino.strftime('%d/%m/%Y')}")

    def clean(self):
        if self.previsao_termino and self.inicio:
            if self.previsao_termino < self.inicio:
                raise ValidationError({
                    "previsao_termino": "A previsão de término não pode ser anterior a data de início."
                })

        if self.fim and self.inicio:
            if self.fim < self.inicio:
                raise ValidationError({
                    "fim": "A previsão de término deve ser igual ou posterior à data de início."
                })