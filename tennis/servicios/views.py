from django.shortcuts import get_object_or_404, render, redirect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.http import HttpResponse
from .models import Servicio, Contratacion
from .forms import ServicioForm, ContratacionForm

# Create your views here
def listaServicio(request):
    servicio=Servicio.objects.all()
    return render(request,"CrudServicio/listado.html",{'servicio':servicio})

def inicio(request):
    return render(request,'paginas_base/inicio.html')

def nosotros(request):
    return render(request,'paginas_base/nosotros.html')      
  
def crear_editarServicio(request,idServicio=0):
      if request.method=="GET":
        if idServicio==0:
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
        
        

# Create your views here
def listaContratacion(request):
    contratacion=Contratacion.objects.all()
    return render(request,"CrudContratacion/listado.html",{'contratacion':contratacion})

def crear_editarContratacion(request, idContratacion=None):
    """
    Maneja tanto la creación como la edición de Contratacion.
    - Si idContratacion es None o 0: se crea una nueva Contratacion.
    - Si idContratacion es un id válido: se edita la Contratacion existente.
    """
    if idContratacion in (0, None):
        contratacion = None
    else:
        contratacion = get_object_or_404(Contratacion, pk=idContratacion)

    if request.method == "POST":
        if contratacion is None:
            formulario = ContratacionForm(request.POST)
        else:
            formulario = ContratacionForm(request.POST, instance=contratacion)

        if formulario.is_valid():
            contrato = formulario.save(commit=False)
            contrato.save()
            formulario.save_m2m()  # guarda relaciones ManyToMany
            return redirect('listaContratacion')
    else:
        if contratacion is None:
            formulario = ContratacionForm()
        else:
            formulario = ContratacionForm(instance=contratacion)

    return render(request, 'CrudContratacion/Crear.html', {'formulario': formulario})


def eliminarContratacion(request, idContratacion):
    bc = Contratacion.objects.get(idContratacion=idContratacion)
    bc.delete()
    return redirect('listaContratacion')
        
         
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 
 