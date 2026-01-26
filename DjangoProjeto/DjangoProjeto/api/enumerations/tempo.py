from django.db import models

class Tempo(models.TextChoices):
    SEGUNDO = "S", "Segundos"
    MINUTO = "MI", "Minutos"
    HORA = "H", "Horas"
    DIA = "D", "Dias"
    SEMANA = "W", "Semanas"
    MES = "MO", "Meses"
    ANO = "A", "Anos"