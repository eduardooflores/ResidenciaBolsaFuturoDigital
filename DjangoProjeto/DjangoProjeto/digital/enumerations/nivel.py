from django.db import models


class Nivel(models.TextChoices):
    BASICO = "Basico", "Básico"
    TECNICO = "Tecnico", "Técnico"
    SUPERIOR = "Superior", "Superior"
    POS = "Pos-Graduacao", "Pós-Graduação"
