from django.db import models


class Operador(models.TextChoices):
    ADICAO = "+", "Adição"
    SUBTRACAO = "-", "Subtração"
    MULTIPLICACAO = "*", "Multiplicação"
    DIVISAO = "/", "Divisão"
    EXPONENCIACAO = "^", "Exponenciação"
    RADICIACAO = "**", "Radiciacao"
    PERCENTAGEM = "%", "Percentagem"
    MODULO = "//", "Modulo"
