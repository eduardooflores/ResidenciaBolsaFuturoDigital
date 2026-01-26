from django.db import models


class PeriodoLetivo(models.TextChoices):
    SEMESTRAL = "Semestral", "Semetral"
    ANUAL = "Anual", "Anual"
    MODULAR = "Modular", "Modular"