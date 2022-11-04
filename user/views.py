from distutils.log import error
from msilib.schema import ListView
from multiprocessing import context
from pyexpat import model
from re import template
from turtle import title
from venv import create
from django import dispatch
import django
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from user.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

# Create your views here.

"""class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'gestionAsociados\listaUsers.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in User.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'ha ocurrido un error'
        except Exception as e:
            data['error']=str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Usuarios'
        context['create_url'] = '' #reverse_lazy('erp')
        context['list_url'] = reverse_lazy('user:user_list')
        context['entity'] = 'Usuarios'
        return context"""


def lista(request):
    usuarios = User.objects.all()
    contexto = {
        'usuarios':usuarios
    }
    return render(request, "gestionAsociados\listaUsers.html", contexto)


def userEstado(request, id ):
    usuario = User.objects.get(id=id)
    if usuario.is_active == False:
        usuario.is_active = True
    else:
        usuario.is_active = False
    usuario.save()
    return redirect("/lista")