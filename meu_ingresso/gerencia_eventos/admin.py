from django.contrib import admin

from gerencia_eventos.models import Evento, Ingresso, Assento

# Register your models here.
admin.site.register(Evento)
admin.site.register(Ingresso)
admin.site.register(Assento)