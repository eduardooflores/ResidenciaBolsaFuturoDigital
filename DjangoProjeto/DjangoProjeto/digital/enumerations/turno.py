from django.db import models

class Turno(models.TextChoices):
    MANHA = "Manha", "Manhã"
    TARDE = "Tarde", "Tarde"
    NOITE = "Noite", "Noite"