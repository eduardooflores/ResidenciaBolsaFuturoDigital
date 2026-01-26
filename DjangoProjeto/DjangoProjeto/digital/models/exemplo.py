from digital.models import BaseModel
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models
from datetime import date
from digital.validators import validar_maioridade

from digital.validators.nome_proibido_validator import NomeProibidoValidator

from digital.enumerations.campus import Campus


class Exemplo(BaseModel):
    nome = models.CharField(max_length=50,
                            validators=[MinLengthValidator(2,
                            message="No mínimo o nome deve conter 2 caracteres"),
                                        NomeProibidoValidator(nomes_proibidos=["admin"])])

    apelido = models.CharField(max_length=50, null=True, blank=True,)

    idade = models.IntegerField(help_text="Idade do exemplo",
                                verbose_name="Insira a idade do exemplo",
                                validators=[MinValueValidator(18, message="Idade mínima 18 anos"),
                                            MaxValueValidator(100, message="Idade máxima 100")])

    nascimento = models.DateField(help_text="Insira a sua data de nascimento",
                                  verbose_name="Data de nascimento",
                                  null=True, blank=True,
                                  validators=[validar_maioridade])

    campus = models.CharField(max_length=30, null=True, blank=True,
                              help_text="Digite o campus de sua escolha",
                              verbose_name="Campus",
                              choices=Campus, default=Campus.PORTO_ALEGRE,
                              validators=[MinLengthValidator(3)])

    def __str__(self):
        return f"{self.id} - {self.nome}"

    # Validado crossfield
    def clean(self):

        # Validação idade -- nascimento
        if self.nascimento != None and self.nascimento != "":
            hoje = date.today()
            idade_calculada = int((hoje - self.nascimento).days / 365.25) # Diferença em dias
            print(idade_calculada,self.idade)
            if idade_calculada != self.idade:
                raise ValidationError({
                    "idade": "Idade incorreta para o nascimento informado",
                    "nascimento": "Nascimento incorreto para a idade informada"
            })

        ## Validação igualdade entre nome e apelido
        if self.apelido != None and self.apelido != "":
            if self.nome.lower() == self.apelido.lower():
                raise ValidationError({
                    "nome": "Apelido não pode ser igual a nome",
                    "apelido": "Nome não pode ser igual a apelido"
            })

    # método que permite alterar campos antes de realizar a persistência dos dados
    def save(self, *args, **kargs):
        if self.nascimento == None or self.nascimento == "":
            hoje = date.today()
            data_nascimento_calcula = hoje.replace(year=hoje.year - self.idade)

            self.nascimento = data_nascimento_calcula
        super().save(*args, **kargs)