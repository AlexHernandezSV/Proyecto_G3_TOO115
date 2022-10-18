#from socket import fromshare
from django import forms



class registerAspirantForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=30)
    apellido = forms.CharField(label ="Apellido",max_length=30)
    email = forms.EmailField()


