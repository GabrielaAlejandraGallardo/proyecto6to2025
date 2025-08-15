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
from django.db.models import Max
from django.db.models.functions import TruncMonth
from django.db.models import Sum

# Create your views here
def listaServicio(request):
    servicio=Servicio.objects.all()
    return render(request,"CrudServicio/listado.html",{'servicio':servicio})

def inicio(request):
    return render(request,'paginas_base/inicio.html')

def nosotros(request):
    return render(request,'paginas_base/nosotros.html')      
  



def crear_editarServicio(request, idServicio):
    if idServicio != 0:
        servicio = get_object_or_404(Servicio, pk=idServicio)
    else:
        # Usar el nombre correcto del campo de clave primaria
        ultimo_id = Servicio.objects.aggregate(Max('idServicio'))['idServicio__max']
        nuevo_id = (ultimo_id or 0) + 1
        servicio = Servicio(idServicio=nuevo_id)

    if request.method == 'POST':
        formulario = ServicioForm(request.POST, instance=servicio)
        if formulario.is_valid():
            formulario.save()
            return redirect('listaServicio')
    else:
        formulario = ServicioForm(instance=servicio)

  
    return render(request, 'CrudServicio/Crear.html', {'formulario': formulario})

def eliminarS(request, idServicio):
    bc=Servicio.objects.get(pk=idServicio)
    bc.delete()
    return redirect('listaServicio')
        

def listaContratacion(request):
    contrataciones = Contratacion.objects.all().prefetch_related('servicios')

    # Total general acumulado
    total_general = sum(
        sum(servicio.costo for servicio in c.servicios.all())
        for c in contrataciones
    )

    # Totales por mes
    contrataciones_por_mes = (
        Contratacion.objects
        .annotate(mes=TruncMonth('fecha'))
        .values('mes')
        .annotate(total_mes=Sum('servicios__costo'))
        .order_by('mes')
    )

    return render(request, 'CrudContratacion/listado.html', {
        'contrataciones': contrataciones,
        'total_general': total_general,
        'contrataciones_por_mes': contrataciones_por_mes,
    })

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
        
         
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 
 