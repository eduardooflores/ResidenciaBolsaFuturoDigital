from digital.models import BaseModel
from django.db import models


class Atleta(BaseModel):
    nome = models.CharField(max_length=50,
                            help_text="Insira o nome do Atleta",
                            verbose_name="Nome do Atleta")

    esporte = models.CharField(max_length=50,
                               help_text="Insira o nome do esporte",
                               verbose_name="Nome do esporte práticado")

    nascimento = models.DateField(help_text="Insira a data de nascimento",
                                  verbose_name="Data de nascimento do atleta",)

    email = models.EmailField(max_length=254,
                              help_text="Insira o email",
                              verbose_name="Insira o e-mail do atleta")

    patrocinio = models.DecimalField(max_digits=5,
                                     decimal_places=2,
                                     help_text="Insira o valor dos patrocionos",
                                     verbose_name="Valor total de patrocinios do alteta")

    premios = models.IntegerField(help_text="Insira a quantidade de prêmios ganhos",
                                  verbose_name="Total de prêmios",)

    nota = models.FloatField(help_text="Insira a nota do aluno",
                             verbose_name="Notas do aluno")

    aposentado = models.BooleanField(help_text="Atleta aposentado",
                                     verbose_name="Aposetado")


    def _str_(self):
        return (f"{self.id} - {self.nome} - {self.esporte} - {self.nascimento} - {self.email} - {self.email}"
                f"{self.patrocinio} - {self.premios} - {self.nota} - {self.aposentado}")