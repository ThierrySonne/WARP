from django.db import models

class Financimento(models.Model):
    tipo = models.CharField('Tipo',max_length=60)
    quantidade = models.CharField('Quantidade',max_length=10)


    class Meta:
        verbose_name = 'Financiamento'
        verbose_name_plural = 'Financiamentos'

    def __str__(self):
        return self.nome
