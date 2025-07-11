from django.db import models


class Agente(models.Model):
    nome = models.CharField('Nome', max_length=60, help_text='Nome do Agente')
    cpf = models.CharField('CPF', max_length=18, help_text='CPF do Agente', unique=True)
    email = models.CharField('Email', max_length=30, help_text='Email do Agente')
    ong = models.ForeignKey('ongs.Ong', verbose_name='ONG', help_text='ONG de Atuação',
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Agente'
        verbose_name_plural = 'Agentes'

    def __str__(self):
        return self.nome