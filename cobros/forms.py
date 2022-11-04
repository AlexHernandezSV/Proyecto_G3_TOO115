import django
from django.forms import modelformset_factory
from gestionAsociados.models import ReciboIngreso

from django import forms
from cobros.models import *

class registerCuotaForm(forms.Form):
    tipo = forms.ChoiceField(label="Tipo")
    monto = forms.FloatField(label="Monto")
    fecha_inicio = forms.DateField(label="Fecha de inicio",input_formats=['%d/%m/%Y'])
    fecha_fin = forms.DateField(label="Fecha fin")

ReciboIngresoFormSet = modelformset_factory(
    ReciboIngreso,
    exclude=(),
    widgets={
        'monto': forms.TextInput(attrs={'class':'form-control'}),
        'descripcion': forms.TextInput(attrs={'class':'form-control'}),
        'tipo': forms.TextInput(attrs={'class':'form-control'}),
        'aspirante': forms.NumberInput(attrs={'class':'form-control'}),
    }
)