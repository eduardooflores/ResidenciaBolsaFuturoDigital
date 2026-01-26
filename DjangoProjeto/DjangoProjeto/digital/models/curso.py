from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from .base_model import BaseModel

from ..enumerations import PeriodoLetivo, Nivel, Turno, Campus


class Curso(BaseModel):
    nome = models.CharField(max_length=50, validators=[MinLengthValidator(5),],)

    nivel = models.CharField(max_length=30, help_text="Escolha o nível do curso",
                             verbose_name="Curso",
                             choices=Nivel, default=Nivel.SUPERIOR)

    duracao = models.IntegerField(help_text="Digite a duração do período letivo",
                                  verbose_name="Período",
                                  validators=[MinValueValidator(1), MaxValueValidator(15),],)

    periodo_letivo = models.CharField(max_length=30, help_text="Escolha o período letivo do Aluno",
                                      verbose_name="Período",
                                      choices=PeriodoLetivo, default=PeriodoLetivo.SEMESTRAL)

    turno = models.CharField(max_length=30, help_text="Escolha o turno do Aluno",
                             verbose_name="Turno",
                             choices=Turno, default=Turno.NOITE)

    campus = models.CharField(max_length=30, help_text="Digite o campus de sua escolha",
                              verbose_name="Campus",
                              choices=Campus, default=Campus.PORTO_ALEGRE,
                              validators=[MinLengthValidator(3)])

    nota_mec = models.FloatField(help_text="Digite a nota do curso",
                                 verbose_name="Nota MEC",
                                 validators=[MinValueValidator(1), MaxValueValidator(5),],)

    def __str__(self):
        return f"{self.nome} - {self.nivel} - {self.duracao} - {self.periodo_letivo} - {self.turno} - {self.campus} - {self.nota_mec}"