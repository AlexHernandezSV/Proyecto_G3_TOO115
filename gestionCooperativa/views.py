from django.shortcuts import redirect, render
from gestionCooperativa.models import DatosCoop
from django.contrib import messages


# Create your views here.

#pagina de ver info de coop
def verInfoCoop(request):
    #mostrar datos
    mostrar= DatosCoop.objects.all()


    return render(request,'gestionCooperativa/verInfoCoop.html', {'mostrar':mostrar})


#Guardar a base de datos
def editarInfoCoop(request):
    mostrar= DatosCoop.objects.all()
    if request.method == "POST":
        #Borrar fila
        entries= DatosCoop.objects.all()
        entries.delete()


        ins = DatosCoop()
        ins.nombre_text= request.POST['nombre']
        ins.departamento_text= request.POST['departamento']
        ins.municipio_text= request.POST['municipio']
        ins.numeroRegistro_text= request.POST['registro']
        ins.aniosFuncionando_numero= request.POST['anios']
        ins.numeroEmpleados_numero= request.POST['empleados']
        ins.descripcion_text= request.POST['descripcion']
        if len(request.FILES) != 0:
            ins.logo_img = request.FILES['image']
        
        ins.save()
        messages.success(request, "Datos Guardados")
        return redirect("/verInfoCoop")

    return render(request,"gestionCooperativa/editarInfoCoop.html", {'mostrar':mostrar})