from django.db import models

class Ong(models.Model):
    nome = models.CharField('Nome', max_length=60, help_text='Nome da ONG')
    cnpj = models.CharField('Cnpj', max_length=18, help_text='CNPJ da ONG', unique=True)
    fone = models.CharField('Fone', max_length=15, help_text='Telefone da ONG')
    ramo = models.CharField('Ramo', max_length=100, help_text='Ramo de atuação da ONG')
    escala = models.CharField('Escala', max_length=10, help_text='Escala da ONG')


    class Meta:
        verbose_name = 'ONG'
        verbose_name_plural = 'ONGs'

    def __str__(self):
        return self.nome