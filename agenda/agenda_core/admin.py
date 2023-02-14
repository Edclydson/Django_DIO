from django.contrib import admin
from .models import Evento
# Register your models here.


class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo_evento', 'data_evento', 'data_criacao')


admin.site.register(Evento, EventoAdmin)
