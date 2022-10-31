import os
from turtle import pd
import django 
import pandas

def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE","Proyecto_G3_TOO115.settings")
    django.setup()
    from gestionAsociados.models import Pais
    direccion_archivo=open(os.path.dirname(os.path.abspath(__file__))+"\datos_paises2.xlsx")
    print("la direccion que estoy cargando es: {}".format(direccion_archivo.name))
    try:
        print('hola0')
        open_file= pandas.read_excel(direccion_archivo.name, engine='openpyxl')
        print('hola1')
        try:
            print('hola2')
            for valor in open_file.values:
                temp_pais= Pais(codigo=valor[2],nombre=valor[0], extensionTelefono = valor[4])
                temp_pais.save()
        except Exception as error:
            print("Ocurrio un error 1. En la clase: {}".format(type(error).__name__))
    except Exception as error:
        print("Ocurrio un error. En la clase: {}".format(type(error).__name__))
if __name__=="__main__":
    main()