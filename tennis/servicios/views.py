from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render, redirect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.http import HttpResponse
from .models import Servicio, Contratacion
from .forms import ServicioForm, ContratacionForm
from django.db import models
from django.conf import settings
from django.contrib.staticfiles.urls import static
# Create your views here
def listaServicio(request):
    servicio=Servicio.objects.all()
    return render(request,"CrudServicio/listado.html",{'servicio':servicio})

def inicio(request):
    return render(request,'paginas_base/inicio.html')

def nosotros(request):
    return render(request,'paginas_base/nosotros.html')      
  
def crear_editarServicio(request,idServicio=None):
      if request.method=="GET":
        if idServicio==None:
            formulario=ServicioForm()   
        else:
            Servicioid=Servicio.objects.get(pk=idServicio)
            formulario=ServicioForm(instance=Servicioid)
        return render(request,'CrudServicio/Crear.html',{'formulario':formulario})
      else:
        if idServicio==0:
            formulario=ServicioForm(request.POST or None, request.FILES or None)
        else:
            Servicioid=Servicio.objects.get(pk=idServicio)
            formulario=ServicioForm(request.POST or None, request.FILES or None ,instance=Servicioid)            
        if formulario.is_valid():
            formulario.save()
        return redirect('listaServicio')
        
def eliminarS(request, idServicio):
    bc=Servicio.objects.get(pk=idServicio)
    bc.delete()
    return redirect('listaServicio')
        
        
def listaContratacion(request):
    contrataciones = Contratacion.objects.all()
    return render(request, 'CrudContratacion/listado.html', {'contrataciones': contrataciones})

def crear_editarContratacion(request, idContratacion=None):
    if idContratacion in [None, 0, '0']:
        contratacion = None
    else:
        contratacion = get_object_or_404(Contratacion, pk=idContratacion)

    if request.method == 'POST':
        formulario = ContratacionForm(request.POST, instance=contratacion)
        if formulario.is_valid():
            nueva = formulario.save(commit=False)
            nueva.save()

            servicios_ids = request.POST.getlist('servicio[]')
            nueva.servicios.set(servicios_ids)

            total = sum(Servicio.objects.get(idServicio=sid).costo for sid in servicios_ids)
            nueva.total_costo = total
            nueva.save()

            return redirect('listaContratacion')
        else:
            print("Errores del formulario:", formulario.errors)
    else:
        formulario = ContratacionForm(instance=contratacion)

    servicios = Servicio.objects.all()
    return render(request, 'CrudContratacion/Crear.html', {
        'formulario': formulario,
        'servicios': servicios
    })




def eliminarContratacion(request, idContratacion):
    bc = Contratacion.objects.get(idContratacion=idContratacion)
    bc.delete()
    return redirect('listaContratacion')
        
         
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 
 