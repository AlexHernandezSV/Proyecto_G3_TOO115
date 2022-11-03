#from socket import fromshare
from django import forms
#from gestionAsociados.models import DatosCoop

#class DatosCoopForm(forms.Form):
#    class Meta:
#        model = DatosCoop
#        fields = ['nombre_text', 'numeroRegistro_text', 'aniosFuncionando_numero', 'numeroEmpleados_numero', 'municipio_text', 'departamento_text', 'logo_img']

class getId(forms.Form):
    #override de __init__ para pasar argumento
     def __init__(self,site_id,*args,**kwargs):
          # llamar __init__ normal
          super().__init__(*args,**kwargs)
          #extender __init__
          self.label_suffix = ""
          self.fields['test']=forms.CharField(label=site_id , max_length=30)        
          print(site_id)
          
          


          

    


    