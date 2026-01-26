from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from digital.enumerations import Predio, Campus
from digital.models import BaseModel


class Escritorio(BaseModel):
    numero = models.IntegerField(help_text="Insira o número da sala",
                                 verbose_name="Número",
                                 validators=[MinValueValidator(1),
                                             MaxValueValidator(100),])

    andar = models.IntegerField(help_text="Insira o andar da sala",
                                verbose_name="Andar",
                                validators=[MinValueValidator(0),
                                            MaxValueValidator(10),])

    predio = models.CharField(max_length=30, choices=Predio,
                              help_text="Selecione o prédio da sala")

    campus = models.CharField(max_length=30, choices=Campus,
                              verbose_name="Campus",
                              help_text="Selecione o campus da sala")

    def __str__(self):
        return f"{self.numero} - {self.andar} - {self.predio} - {self.campus}"