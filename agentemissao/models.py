from django.db import models

class AgenteMissao(models.Model):
    agente = models.ForeignKey('agentes.Agente', verbose_name='Agente',help_text='Nome do agente',
                               on_delete=models.CASCADE, related_name='agente')
    desastre = models.ForeignKey('desastres.Desastre', verbose_name='Desastre', help_text='Nome do desastre',
                                 on_delete=models.CASCADE, related_name='desastre')
    abrigo = models.ForeignKey('abrigos.Abrigo', verbose_name='Abrigo', help_text='Nome do abrigo',
                               on_delete=models.CASCADE, related_name='abrigo')
    funcao = models.CharField('Função',max_length=30,help_text='Função do agente')
    duracao = models.CharField('Duração',max_length=20, help_text='Duração da missão')

    class Meta:
        verbose_name = 'Missão do agente'
        verbose_name_plural = 'Missões do agente'


    def __str__(self):
        return f'{self.agente}'
