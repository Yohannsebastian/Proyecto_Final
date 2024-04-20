from django import forms
from .models import Formulario                   

class Form(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ['nombre', 'apellido', 'correo', 'mensaje']
        widgets = {
            'mensaje': forms.Textarea()
        }