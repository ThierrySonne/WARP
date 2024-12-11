from django import forms

from ongs.models import Ong
from .models import Agente

class AgenteListForm(forms.Form):
    ongs = forms.ModelChoiceField(label='Ong', queryset=Ong.objects.all(), required=False)

class AgenteModelForm(forms.ModelForm):
    class Meta:
        model = Agente
        fields = 'nome','cpf','fone','ong'

        error_messages = {
            'nome': {'required': 'O nome do Agente é um campo obrigatório'},
            'cpf': {'required': 'O CPF do Agente é um campo obrigatório', 'unique': 'CPF já cadastrado'},
            'fone': {'required': 'O número de telefone é um campo obrigatório'},
            'ong': {'required': 'O Ramo do Agente é um campo obrigatório'},
        }

