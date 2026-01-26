from django.db import models

class TipoProjeto(models.TextChoices):
    WEB = "Desenvolvimento Web", "Desenvolvimento Web"
    MOBILE = "Aplicativo de Celular", "Aplicativo de Celular"
    DESKTOP = "Aplicação Desktop", "Aplicação Desktop"
    API = "Web Services/API", "Web Services/API"
    LIBRARY = "Biblioteca/SDK", "Biblioteca/SDK"
    DATA_SCIENCE = "Projeto de Ciência de Dados", "Projeto de Ciência de Dados"
    AI = "Inteligência Artificial", "Inteligência Artificial"