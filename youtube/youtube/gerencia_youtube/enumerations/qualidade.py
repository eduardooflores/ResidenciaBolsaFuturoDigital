from django.db import models

class Qualidade(models.TextChoices):
    BAIXA_360 = 360, "360"
    BAIXA_480 = 480, "480"
    MEDIA_720 = 720, "720"
    ALTA_1080 = 1080, "1080"
    MUITO_ALTA = 1440, "1440"
    EXTREMAMENTE_ALTA = 2160, "2160"
