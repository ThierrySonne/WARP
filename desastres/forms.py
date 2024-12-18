from django import forms

from .models import Desastre

class DesastreModelForm(forms.ModelForm):
    class Meta:
        model = Desastre
        fields = 'nome','tipo','data','local','populacao','foto'

        error_messages = {
            'nome': {'required': 'O nome do Desastre é um campo obrigatório'},
            'tipo': {'required': 'O tipo do Desastre é um campo obrigatório'},
            'data': {'required': 'A data do Desastre é um campo obrigatório'},
            'local': {'required': 'O local do Desastre é um campo obrigatório'},
            'populacao': {'required': 'A quantidade de Vítimas é um campo obrigatório'},
            'foto': {'required:': 'Imagem Obrigatória'},
        }