from datetime import date, datetime
from django.shortcuts import redirect, render
from psycopg2 import Date
from django.contrib.auth.decorators import login_required
from cobros.forms import registerCuotaForm,ReciboIngresoFormSet
from .models import Cuota
from gestionAsociados.models import ReciboIngreso

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


def listaRecibos(request):
    if verificarRol('cajero',request.user):

        if request.method == 'POST':
            filtro = request.POST['filtro']
            print(filtro)
            if filtro == 'all':
                recibosFiltrados = ReciboIngreso.objects.all()
            else:
                recibosFiltrados = ReciboIngreso.objects.filter(cancelado=filtro)
            return render(request,'listaRecibos.html',{"recibos":recibosFiltrados})
    else:
        return redirect('/home')
        
    recibos = ReciboIngreso.objects.all()
    #recibosPendientes = recibos.filter(cancelado = False)
    return render(request,'listaRecibos.html',{"recibos":recibos,})

@login_required
def cancelarReciboIngreso(request,id):
    recibo = ReciboIngreso.objects.get(id=id)
    recibo.cancelado = True
    recibo.save()
    return redirect('/gestionar_recibos')

def verificarRol(rolrequerido,user):
    if rolrequerido == user.role or rolrequerido.upper() == user.role:
        return True
    else:
        return False