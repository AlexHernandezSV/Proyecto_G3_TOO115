#from socket import fromshare
from django import forms
from gestionAsociados.models import DatosCoop

class DatosCoopForm(forms.Form):
    class Meta:
        model = DatosCoop
        fields = ['nombre_text', 'numeroRegistro_text', 'aniosFuncionando_numero', 'numeroEmpleados_numero', 'municipio_text', 'departamento_text', 'logo_img']

