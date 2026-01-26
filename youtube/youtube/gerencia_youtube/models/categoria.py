from django.core.validators import MinLengthValidator

from .base_model import BaseModel
from django.db import models

class Categoria(BaseModel):

    nome = models.CharField(max_length=100,
                            validators=[MinLengthValidator(3)],
                            verbose_name="Categoria",
                            help_text="Digite o nome da categoria",
                            unique=True)

    def __str__(self):
        return f"{self.nome}"