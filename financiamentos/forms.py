from django import forms

from .models import Financiamento

class FinanciamentoModelForm(forms.ModelForm):
    class Meta:
        model = Financiamento
        fields = 'nome','tipo','quantidade'

        error_messages = {
            'nome': {'required': 'O ID do Financiamento é um campo obrigatório'},
            'tipo': {'required': 'O tipo de Financiamento é um campo obrigatório'},
            'quantidade': {'required': 'A quantia a ser doada é um campo obrigatório'},
        }