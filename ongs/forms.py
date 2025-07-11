from django import forms

from .models import Ong

class OngModelForm(forms.ModelForm):
    class Meta:
        model = Ong
        fields = 'nome','cnpj','fone','ramo','escala','foto'

        error_messages = {
            'nome': {'required': 'O nome da ONG é um campo obrigatório'},
            'cnpj': {'required': 'O Cnpj da ONG é um campo obrigatório', 'unique': 'Cnpj já cadastrado'},
            'fone': {'required': 'O número de telefone é um campo obrigatório'},
            'ramo': {'required': 'O Ramo da ONG é um campo obrigatório'},
            'escala': {'required': 'A Escala da Organização é um campo obrigatório'},
        }
