import os
import json
import django 

def main():
    #indicar que utilize el archivo settings
    os.environ.setdefault("DJANGO_SETTINGS_MODULE","Proyecto_G3_TOO115.settings")
    django.setup()
    from gestionAsociados.models import Municipio, Departamento
    datos_departamentos=open(os.path.dirname(os.path.abspath(__file__))+"\departamentos.json")
    datos_departamentos= json.load(datos_departamentos)
    for departamento in datos_departamentos:
        nuevo_departamento= Departamento(codigo=departamento['id'],
                                         nombre=departamento['nombre'])
        nuevo_departamento.save()
        departamento_temporal= Departamento.objects.get(codigo=departamento['id'])
        for municipios in departamento['municipios'] :
            municipio=Municipio(codigo=municipios['id_mun'],
                                nombre=municipios['nombre'],
                                departamento=departamento_temporal,)
            municipio.save()
if __name__=="__main__":
    main()