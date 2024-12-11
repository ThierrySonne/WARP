from django import forms

from .models import Financimento

class FinanciamentoModelForm(forms.ModelForm):
    class Meta:
        model = Financimento
        fields = 'tipo','quantidade'

        error_messages = {
            'nome': {'required': 'O tipo de Financiamento é um campo obrigatório'},
            'cpf': {'required': 'A quantia a ser doada é um campo obrigatório'},
        }