from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from wrapper.enumerations import Genero
from wrapper.models import BaseModel, Cidade, Time, Esporte


class Pessoa(BaseModel):
    nome = models.CharField(max_length=30,
                            validators=[MinLengthValidator(2)],
                            verbose_name="Nome",
                            help_text="Insira o nome da pessoa")

    genero = models.CharField(max_length=15,
                              validators=[MinLengthValidator(5)],
                              choices=Genero,
                              verbose_name="Gênero",
                              help_text="Selecione o gênero da pessoa")

    idade = models.IntegerField(validators=[MinValueValidator(0),
                                            MaxValueValidator(150)],
                                verbose_name="Idade",
                                help_text="Insira a idade da pessoa")

    renda = models.DecimalField(max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(0.00),
                                            MaxValueValidator(100000000.00)],
                                help_text="Valor da renda mensal",
                                verbose_name="Renda Mensal")

    endereco = models.ForeignKey(Cidade,
                                 on_delete=models.RESTRICT,
                                 verbose_name="Endereço",
                                 help_text="Selecione a cidade")

    time = models.ForeignKey(Time,
                             on_delete=models.RESTRICT,
                             verbose_name="Time que torce",
                             help_text="Selecione o  time que a pessoa torce")

    esporte = models.ForeignKey(Esporte,
                                on_delete=models.RESTRICT,
                                verbose_name="Esporte favorito",
                                help_text="Selecione o esporte favorito")

    def __str__(self):
        return f"{self.nome} - {self.idade} - {self.renda}"