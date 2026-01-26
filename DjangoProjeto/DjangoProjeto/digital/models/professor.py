from django.core.validators import MinLengthValidator
from django.db import models

from digital.models import BaseModel, Escritorio

from digital.validators.admissao_validator import AdmissaoValidator


class Professor(BaseModel):
    matricula = models.CharField(max_length=7, unique=True,
                                 validators=[MinLengthValidator(7),],
                                 help_text="Insira a matrícula do Professor",
                                 verbose_name="Matrícula")

    nome = models.CharField(max_length=50, validators=[MinLengthValidator(2),],
                            help_text="Digite o nome do Professor")


    area = models.CharField(max_length=50,
                            validators=[MinLengthValidator(4),],
                            help_text="Digite a área do professor",
                            verbose_name="Área")

    admissao = models.DateField(help_text="Digite a data de admissão",
                                verbose_name="Admissão",
                                validators=[AdmissaoValidator(),]
                                )

    email = models.EmailField(verbose_name="E-mail", unique=True,
                              help_text="Digite o e-mail profissional do professor",
                              # TODO: CRIAR UM VALIDADOR PARA ACEITAR APENAS E-MAIL PROFISSIONAL
                              )

    aposentado = models.BooleanField(default=False,
                                     verbose_name="Aposentado ?",
                                     help_text="Marque se o professor está aposentado")

    horario_inicial = models.TimeField(verbose_name="Hora de início do trabalho",
                                       help_text="Digite a hora de início do trabalho")

    # TODO: CRIAR VALIDADOR PARA O HORÁRIO FINAL SER POSTERIOR AO INICIAL
    horario_final = models.TimeField(verbose_name="Hora de término do trabalho",
                                     help_text="Digite a hora de término do trabalho")

    escritorio = models.OneToOneField(Escritorio,
                                      on_delete=models.CASCADE,
                                      verbose_name="Escritório", help_text="Escolha o escritório")

    def __str__(self):
        return f"{self.matricula} - {self.nome} - {self.escritorio}"