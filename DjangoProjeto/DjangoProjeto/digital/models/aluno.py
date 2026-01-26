from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from digital.managers.aluno import AlunoManager
from digital.models import BaseModel, Disciplina


class Aluno(BaseModel):
    matricula = models.CharField(max_length=7, unique=True,
                                 validators=[MinLengthValidator(7),],
                                 help_text="Insira a matrícula do Aluno",
                                 verbose_name="Matrícula")

    nome = models.CharField(max_length=50,
                            validators=[MinLengthValidator(2),],
                            help_text="Insira o nome do Aluno",
                            verbose_name="Nome")

    ingresso = models.DateField(help_text="Digite a data de ingresso",
                                verbose_name="Ingresso",
                                # TODO: INgresso VALIDATOR
                                validators=[],)

    email = models.EmailField(verbose_name="E-mail", unique=True,
                              help_text="Digite o e-mail do aluno",)

    formando = models.BooleanField(default=False,
                                   verbose_name="Formando ?",
                                   help_text="Marque se o Aluno está se formando",)

    bolsista = models.DecimalField(max_digits=7, decimal_places=2,
                                   validators=[MinValueValidator(0),],
                                   help_text="Insira o valor da bolsa",
                                   verbose_name="Valor total da bolsa do Aluno")

    nascimento = models.DateField(help_text="Insira a data de nascimento",
                                  verbose_name="Data de nascimento do atleta",)

    media = models.FloatField(help_text="Digite o rendimento do Aluno",
                              verbose_name="Rendimento")

    disciplinas = models.ManyToManyField(Disciplina, null=True, blank=True,
                                         through="Historico", through_fields=("aluno", "disciplina"))

    objects = AlunoManager()

    def __str__(self):
        return (
            self.nome
        )