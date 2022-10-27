from datetime import date, datetime
from django.shortcuts import redirect, render
from psycopg2 import Date

from cobros.forms import registerCuotaForm
from .models import Cuota

# Create your views here.
def tableCuotas(request):
    cuotas = Cuota.objects.all()
    #form = registerCuotaForm()
    return render(request, "createCuota.html",{"cuotas":cuotas})

def RegistrarCuotas(request):
    tipo =  request.POST['tipo']
    monto =  request.POST['txtMonto']
    fecha_inicio =  request.POST['txtFechaInicio']
    fecha_fin =  request.POST['txtFechaFinal']
    cuota = Cuota.objects.create(tipo=tipo, monto=monto, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)
    return redirect("/Cuotas")


"""def EdicionCuotas(request, id):
    cuota = Cuota.objects.get(id=id)
    datos = {
        'cuota':cuota
    }
    return render(request, "editCuota.html",datos)


def EditarCuotas(request):
    monto =  request.POST['txtMonto']

    cuota = Cuota.objects.get(id=id)
    cuota.monto = monto
    cuota.save()

    return redirect('/Cuotas')"""


def EliminarCuotas(request, id):
    cuota = Cuota.objects.get(id=id)
    cuota.delete()
    return redirect("/Cuotas")
