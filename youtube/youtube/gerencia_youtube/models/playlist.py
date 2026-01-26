from django.core.validators import MinLengthValidator

from .base_model import BaseModel
from django.db import models

class Playlist(BaseModel):

    playlist_id = models.CharField(max_length=50,
                                   validators=[MinLengthValidator(11)],
                                   verbose_name="Playlist ID",
                                   help_text="Digite o ID da playlist.",
                                   unique=True)

    playlist_nome = models.CharField(max_length=50,
                                     validators=[MinLengthValidator(1)],
                                     verbose_name="Nome Playlist",
                                     help_text="Digite o nome da playlist.")

    def __str__(self):
        return f"{self.playlist_id} - {self.playlist_nome}"