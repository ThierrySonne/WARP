from django.db import models
from stdimage import StdImageField


class Desastre(models.Model):
    nome = models.CharField('Nome',max_length=60)
    tipo = models.CharField('Tipo',max_length=60)
    data = models.CharField('Data',max_length=20)
    local = models.CharField('Local',max_length=100)
    populacao = models.CharField('População',max_length=10)
    foto = StdImageField('Foto', upload_to='desastres', delete_orphans=True, null=True, blank=True)


    class Meta:
        verbose_name = 'Desastre'
        verbose_name_plural = 'Desastres'

    def __str__(self):
        return self.nome



