from django import forms

from .models import Abrigo

class AbrigoModelForm(forms.ModelForm):
    class Meta:
        model = Abrigo
        fields = 'nome','local','capacidade'

        error_messages = {
            'nome': {'required': 'O nome do Abrigo é um campo obrigatório'},
            'local ': {'required': 'O local do Abrigoé um campo obrigatório'},
            'capacidade': {'required': 'A capacidade é um campo obrigatório'},
            }