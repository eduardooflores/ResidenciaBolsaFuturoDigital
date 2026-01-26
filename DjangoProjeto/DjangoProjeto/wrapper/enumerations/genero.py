from django.db import models


class Genero(models.TextChoices):
    FEMININO = 'Feminino', 'Feminino'
    MASCULUNO = 'Masculino' , 'Masculino'
    OUTRO = 'Outro', 'Outro'