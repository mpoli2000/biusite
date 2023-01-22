from django import forms
from django.forms import ModelForm
from .models import Tablero



#OPCION FORM MODEL
class TableroForm(ModelForm):
    required_css_class = 'form-label'
    class Meta:
        model = Tablero
        fields = ['level', 'size']
        widgets={
                'level':forms.Select(attrs={'class':'form-select'}),
                'size':forms.Select(attrs={'class':'form-select'}),
                }
        labels = {'level': 'Nivel', 'size': 'Tamaño'}



# LEVEL_CHOICES = (
#     ('1', 'bajo'),
#     ('2', 'medio'),
#     ('3', 'alto'),
#     )

# SIZE_CHOICES =(
#     ('2', '2x2'),
#     ('3', '3x3'),
#     )

# OPCION BOOTSTARP DESDE FORM
# class TableroForm(forms.Form):
#     # level = forms.CharField(max_length=3, widget=forms.Select(choices= LEVEL_CHOICES))
#     size = forms.CharField(label='Tamaño', max_length=1, widget=forms.Select(attrs={'class': 'form-select'}, choices= SIZE_CHOICES))
#     level = forms.CharField(label='Nivel', max_length=1, widget=forms.Select(attrs={'class': 'form-select'}, choices= LEVEL_CHOICES))


