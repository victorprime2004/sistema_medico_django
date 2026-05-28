from django import forms

from models import Medico

class MedicoForm(forms.ModelForm):
    class Meta: #  classe Meta serve para configurar o form
        model = Medico # Define o model que o form representa
        fields = ['nome','sobrenome','email','telefone','crm',]