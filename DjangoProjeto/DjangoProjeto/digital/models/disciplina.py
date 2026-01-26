from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

from digital.enumerations import Modalidade
from digital.models import BaseModel
from django.db import models

class Disciplina(BaseModel):
    nome = models.CharField(max_length=30,
                            validators=[MinLengthValidator(5),],
                            help_text="Digite o nome da Disciplina",
                            verbose_name="Disciplina")

    creditos = models.IntegerField(help_text="Digite os creditos da disciplina",
                                   verbose_name="Créditos",
                                   validators=[MinValueValidator(1), MaxValueValidator(8),],)

    carga_horaria = models.IntegerField(help_text="Digite a carga horária da disciplina",
                                        verbose_name="Carga Horária",
                                        validators=[MinValueValidator(20), MaxValueValidator(160),],)

    modalidade = models.CharField(max_length=50,
                                  help_text="Digite a modalidade da disciplima",
                                  verbose_name="Modalidade",
                                  choices=Modalidade)

    data_inicio = models.DateField(help_text="Digite a data de inicio da disciplina",
                                   verbose_name="Data inicio")

    data_fim = models.DateField(help_text="Digite a data de termino da disciplina",
                                verbose_name="Data fim")

    ementa = models.TextField(max_length=2000,
                              help_text="Digite a ementa da disciplina",
                              verbose_name="Ementa",
                              validators=[MinLengthValidator(50),],)

    fechada = models.BooleanField(help_text="A disciplina está desativada ?",
                                  verbose_name="Disciplina fechada",
                                  default=True)


    def __str__(self):
        return f"{self.nome} - {self.creditos} - {self.carga_horaria} - {self.modalidade} - {self.data_inicio} - {self.data_fim} - {self.ementa} - {self.fechada}"

    def clean(self):
        limite = self.data_fim - self.data_inicio
        limite = limite.days
        if limite < 140:
            raise ValueError({
                "inicio": "O fim da disciplina deve ser 20 semanas depois do inicio",
                "fim": "O fim da disciplina deve ser 20 semanas depois do inicio"
            })