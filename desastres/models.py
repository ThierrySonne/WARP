from django.db import models

class Desastre(models.Model):
    nome = models.CharField('Nome',max_length=60)
    tipo = models.CharField('Tipo',max_length=60)
    data = models.CharField('Data',max_length=20)
    local = models.CharField('Local',max_length=100)
    populacao = models.CharField('População',max_length=10)


    class Meta:
        verbose_name = 'Desastre'
        verbose_name_plural = 'Desastres'

    def __str__(self):
        return self.nome



