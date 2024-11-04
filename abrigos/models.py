from django.db import models

class Abrigo(models.Model):
    nome = models.CharField(max_length=60)
    local =models.CharField(max_length=100)
    capacidade = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Abrigo'
        verbose_name_plural = 'Abrigos'

    def __str__(self):
        return self.nome
