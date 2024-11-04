from django import forms

from .models import Abrigo

class AbrigoModelForm(forms.ModelForm):
    class Meta:
        model = Abrigo
        fields = '__all__'

