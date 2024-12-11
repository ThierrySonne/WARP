from django.db import models

class Abrigo(models.Model):
    nome = models.CharField('Nome',max_length=60, help_text='Nome do Abrigo')
    local =models.CharField('Local',max_length=100, help_text='Localização do Abrigo')
    capacidade = models.CharField('Capacidade',max_length=10, help_text='Capacidade do Abrigo')

    class Meta:
        verbose_name = 'Abrigo'
        verbose_name_plural = 'Abrigos'

    def __str__(self):
        return self.nome
