from django import forms
from .models import Remedio

class Remedioforms(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Adicione seu medicamento...'}))
    class Meta:
        model = Remedio
        fields = '__all__'
