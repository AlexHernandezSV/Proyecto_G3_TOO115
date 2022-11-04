from django.shortcuts import render, redirect
from .models import Item
from django.contrib import messages


# Create your views here.

def listaDire(request):
    return render(request, 'listaDirec.html')

def addDirectivo(request):
    if request.method == 'POST':
        directivo = Item()
        directivo.nombreRepresentante = request.POST.get('nombreDirec')
        directivo.cargo = request.POST.get('cargo')
        directivo.firma = request.POST.get('firma')

        if len(request.FILES) != 0:
            directivo.firma = request.FILES['firma']
        
        directivo.save()
        messages.success(request, "Directivo agregaddo correctamente")
        return redirect('/listaDirec')
    return render(request, 'addDirec.html')

def Directivos(request):
    directivo = Item.objects.all()
    context = {'directivos':directivo}
    return render(request, 'listaDirec.html', context)


def EliminarDirectivos(request, id):
    directivo = Item.objects.get(id=id)
    directivo.delete()
    return redirect("/listaDirec")