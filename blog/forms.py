from django import forms
from .models import Libro


class LibroForm(forms.ModelForm):
    class Meta:
        model =Libro
        fields = ["nombre","correo","poblacion"]