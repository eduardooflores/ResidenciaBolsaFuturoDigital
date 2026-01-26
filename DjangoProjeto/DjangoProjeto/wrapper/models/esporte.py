from django.core.validators import MinLengthValidator
from django.db import models

from wrapper.models.base_model import BaseModel


class Esporte(BaseModel):
    nome = models.CharField(max_length=50,
                            verbose_name="Nome do esporte",
                            help_text="Digite o nome do esporte",
                            validators=[MinLengthValidator(3)])

    def __str__(self):
        return f"{self.nome}"