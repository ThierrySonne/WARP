from django import forms
from django.forms import inlineformset_factory

from agentemissao.models import AgenteMissao
from ongs.models import Ong
from .models import Agente

class AgenteListForm(forms.Form):
    ong = forms.ModelChoiceField(label='Ong', queryset=Ong.objects.all(), required=False)

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

AgenteMissaoInLine = inlineformset_factory(Agente, AgenteMissao, fk_name='agente',
                                           fields=('desastre', 'abrigo', 'funcao', 'duracao'), extra=1, can_delete=True)