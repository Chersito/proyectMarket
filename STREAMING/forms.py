from django import forms

from STREAMING.models import Pelis


class FormularioPelis(forms.ModelForm):
    class Meta:
        model = Pelis
        fields = ['titulo', 'sinopsis', 'director', 'fechaLanzamiento']
        labels = {
            'titulo': 'Título',
            'sinopsis': 'Sinopsis',
            'director': 'Director',
            'fechaLanzamiento': 'Fecha de Lanzamiento'
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'sinopsis': forms.Textarea(attrs={'class': 'form-control'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaLanzamiento': forms.DateInput(attrs={'class': 'form-control', 'type':'date','placeholder':'yyyy-mm-dd'}),
        }
