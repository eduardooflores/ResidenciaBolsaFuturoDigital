from django.contrib import admin
from wrapper.models import Pessoa, Cidade, Esporte, Time
# Register your models here.
admin.site.register((Pessoa, Cidade, Time, Esporte))