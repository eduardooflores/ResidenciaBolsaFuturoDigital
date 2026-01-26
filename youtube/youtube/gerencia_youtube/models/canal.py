from django.core.validators import MinLengthValidator

from .base_model import BaseModel
from django.db import models

class Canal(BaseModel):

    canal_id = models.CharField(max_length=50,
                                validators=[MinLengthValidator(10)],
                                verbose_name="Canal ID",
                                help_text="Digite o ID do canal.",
                                unique=True)

    canal_nome = models.CharField(max_length=50,
                                  validators=[MinLengthValidator(1)],
                                  verbose_name="Nome do canal",
                                  help_text="Digite o nome do canal.")

    canal_inscritos = models.IntegerField(verbose_name="Quantidade de inscritos",
                                          help_text="Digite a quantidade de inscritos do canal.")

    def __str__(self):
        return f"{self.canal_id} - {self.canal_nome} - Inscritos:{self.canal_inscritos}"
