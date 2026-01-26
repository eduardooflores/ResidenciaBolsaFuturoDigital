from django.core.validators import MinLengthValidator

from wrapper.models.base_model import BaseModel
from django.db import models


class Time(BaseModel):
    nome = models.CharField(max_length=30,
                            verbose_name="Nome do Clube",
                            help_text="Digite o nome do clube",
                            validators=[MinLengthValidator(3)])

    def __str__(self):
        return f"{self.nome}"