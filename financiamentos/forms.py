from django import forms

from .models import Financimento

class FinanciamentoModelForm(forms.ModelForm):
    class Meta:
        model = Financimento
        fields = '__all__'

