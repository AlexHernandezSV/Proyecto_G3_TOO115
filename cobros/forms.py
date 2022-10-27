import django


from django import forms
from cobros.models import *

class registerCuotaForm(forms.Form):
    tipo = forms.ChoiceField(label="Tipo")
    monto = forms.FloatField(label="Monto")
    fecha_inicio = forms.DateField(label="Fecha de inicio",input_formats=['%d/%m/%Y'])
    fecha_fin = forms.DateField(label="Fecha fin")