from django.contrib import admin

from gerencia_youtube.models import Canal, Categoria, Playlist, Video

# Register your models here.
admin.site.register((Canal, Categoria, Playlist, Video))
