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

class SudokuForm(forms.Form):
        id_0 = forms.CharField(max_length=1, required=False)
        id_1 = forms.CharField(max_length=1, required=False)
        id_2 = forms.CharField(max_length=1, required=False)
        id_3 = forms.CharField(max_length=1, required=False)
        id_4 = forms.CharField(max_length=1, required=False)
        id_5 = forms.CharField(max_length=1, required=False)
        id_6 = forms.CharField(max_length=1, required=False)
        id_7 = forms.CharField(max_length=1, required=False)
        id_8 = forms.CharField(max_length=1, required=False)
        id_9 = forms.CharField(max_length=1, required=False)
        id_10 = forms.CharField(max_length=1, required=False)
        id_11 = forms.CharField(max_length=1, required=False)
        id_12 = forms.CharField(max_length=1, required=False)
        id_13 = forms.CharField(max_length=1, required=False)
        id_14 = forms.CharField(max_length=1, required=False)
        id_15 = forms.CharField(max_length=1, required=False)
        id_16 = forms.CharField(max_length=1, required=False)
        id_17 = forms.CharField(max_length=1, required=False)
        id_18 = forms.CharField(max_length=1, required=False)
        id_19 = forms.CharField(max_length=1, required=False)
        id_20 = forms.CharField(max_length=1, required=False)
        id_21 = forms.CharField(max_length=1, required=False)
        id_22 = forms.CharField(max_length=1, required=False)
        id_23 = forms.CharField(max_length=1, required=False)
        id_24 = forms.CharField(max_length=1, required=False)
        id_25 = forms.CharField(max_length=1, required=False)
        id_26 = forms.CharField(max_length=1, required=False)
        id_27 = forms.CharField(max_length=1, required=False)
        id_28 = forms.CharField(max_length=1, required=False)
        id_29 = forms.CharField(max_length=1, required=False)
        id_30 = forms.CharField(max_length=1, required=False)
        id_31 = forms.CharField(max_length=1, required=False)
        id_32 = forms.CharField(max_length=1, required=False)
        id_33 = forms.CharField(max_length=1, required=False)
        id_34 = forms.CharField(max_length=1, required=False)
        id_35 = forms.CharField(max_length=1, required=False)
        id_36 = forms.CharField(max_length=1, required=False)
        id_37 = forms.CharField(max_length=1, required=False)
        id_38 = forms.CharField(max_length=1, required=False)
        id_39 = forms.CharField(max_length=1, required=False)
        id_40 = forms.CharField(max_length=1, required=False)
        id_41 = forms.CharField(max_length=1, required=False)
        id_42 = forms.CharField(max_length=1, required=False)
        id_43 = forms.CharField(max_length=1, required=False)
        id_44 = forms.CharField(max_length=1, required=False)
        id_45 = forms.CharField(max_length=1, required=False)
        id_46 = forms.CharField(max_length=1, required=False)
        id_47 = forms.CharField(max_length=1, required=False)
        id_48 = forms.CharField(max_length=1, required=False)
        id_49 = forms.CharField(max_length=1, required=False)
        id_50 = forms.CharField(max_length=1, required=False)
        id_51 = forms.CharField(max_length=1, required=False)
        id_52 = forms.CharField(max_length=1, required=False)
        id_53 = forms.CharField(max_length=1, required=False)
        id_54 = forms.CharField(max_length=1, required=False)
        id_55 = forms.CharField(max_length=1, required=False)
        id_56 = forms.CharField(max_length=1, required=False)
        id_57 = forms.CharField(max_length=1, required=False)
        id_58 = forms.CharField(max_length=1, required=False)
        id_59 = forms.CharField(max_length=1, required=False)
        id_60 = forms.CharField(max_length=1, required=False)
        id_61 = forms.CharField(max_length=1, required=False)
        id_62 = forms.CharField(max_length=1, required=False)
        id_63 = forms.CharField(max_length=1, required=False)
        id_64 = forms.CharField(max_length=1, required=False)
        id_65 = forms.CharField(max_length=1, required=False)
        id_66 = forms.CharField(max_length=1, required=False)
        id_67 = forms.CharField(max_length=1, required=False)
        id_68 = forms.CharField(max_length=1, required=False)
        id_69 = forms.CharField(max_length=1, required=False)
        id_70 = forms.CharField(max_length=1, required=False)
        id_71 = forms.CharField(max_length=1, required=False)
        id_72 = forms.CharField(max_length=1, required=False)
        id_73 = forms.CharField(max_length=1, required=False)
        id_74 = forms.CharField(max_length=1, required=False)
        id_75 = forms.CharField(max_length=1, required=False)
        id_76 = forms.CharField(max_length=1, required=False)
        id_77 = forms.CharField(max_length=1, required=False)
        id_78 = forms.CharField(max_length=1, required=False)
        id_79 = forms.CharField(max_length=1, required=False)
        id_80 = forms.CharField(max_length=1, required=False)


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


