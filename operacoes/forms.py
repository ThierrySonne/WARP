from django import forms

from .models import Operacoes
from desastres.models import Desastre
from ongs.models import Ong


class OperacoesListForm(forms.Form):
    desastre = forms.ModelChoiceField(label='Desastre',queryset=Desastre.objects.all(), required=False)
    ong = forms.ModelChoiceField(label='Ong',queryset=Ong.objects.all(), required=False)


class OperacoesModelForm(forms.ModelForm):
    class Meta:
        model = Operacoes
        fields = ['operacao', 'desastre', 'ong']

        error_messages = {
            'operacao': {'required': 'O nome da Operação é um campo obrigatório'},
            'desastre': {'required': 'O nome do Desastre é um campo obrigatório'},
            'ong': {'required': 'O nome da ONG é um campo obrigatório'},
        }