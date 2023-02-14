from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Evento(models.Model):
    titulo_evento = models.CharField(max_length=100,
                                     verbose_name = 'Título do Evento')
    descricao_evento = models.TextField(verbose_name = 'Descrição do Evento')
    data_evento = models.DateTimeField(verbose_name = 'Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True,
                                        verbose_name = 'Data de Criação')
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo_evento
