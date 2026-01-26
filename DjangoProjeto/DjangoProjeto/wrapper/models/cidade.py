from django.core.validators import MinLengthValidator
from django.db import models
from wrapper.models.base_model import BaseModel

class Cidade(BaseModel):
    nome = models.CharField(max_length=50,
                            validators=[MinLengthValidator(3)],
                            verbose_name="Nome da cidade",
                            help_text="Insira o nome da cidade")

    estado = models.CharField(max_length=2,
                              validators=[MinLengthValidator(2)],
                              verbose_name="Estado",
                              help_text="Insira a sigla do Estado")

    def __str__(self):
        return f"{self.nome}/{self.estado}"