from django.db import models


class Operacoes(models.Model):
    operacao = models.CharField('Operação', help_text='Nome da Operação', max_length=100)
    desastre = models.ForeignKey('desastres.Desastre', verbose_name='Desastre', help_text='Nome do desastre',
                                 on_delete=models.CASCADE)
    ong = models.ForeignKey('ongs.Ong', verbose_name='Ong', help_text='Nome do ONG',
                            on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Operação'
        verbose_name_plural = 'Operações'


    def __str__(self):
        return f'Ong: {self.ong}'
