from collections import defaultdict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .forms import CuotaForm
from cuota.models import Cuota

# Create your views here

def listaCuotabORRAR(request):
    cuotas=Cuota.objects.all()
    return render(request,"crudCuotas/listado.html",{'cuotas':cuotas})

def listaCuota(request):
    jugador_cuota = Cuota.objects.all().order_by('cuotaMes')
    pagos_por_mes = defaultdict(list)
    total_por_mes = defaultdict(float)
    pagos_admin = defaultdict(list)
    total_pagos_admin = defaultdict(float)
    for sc in jugador_cuota:
        mes = sc.cuotaMes
        pagos_por_mes[mes].append(sc)
        total_por_mes[mes] += float(sc.importe)
       
             
    # Convertir a lista de tuplas para el template
    pagos_y_totales = [
        (mes, pagos_por_mes[mes], total_por_mes[mes])
        for mes in pagos_por_mes
    ]
    for s in jugador_cuota:
      m = s.cuotaMes
      pagos_admin[mes].append(s)
      diezporciento= total_por_mes[m] * 0.10
      total_pagos_admin[m]+=float(diezporciento)
      totalpagosAadmin=[(m,pagos_admin[m],total_pagos_admin[m])    
                 for m in pagos_admin]

    return render(request, 'CrudSocioCuota/listado.html', {
        'pagos_y_totales': pagos_y_totales, 'totalpagosAadmin': totalpagosAadmin
    })
def inicio(request):
    return render(request,'paginas_base/inicio.html')

def nosotros(request):
    return render(request,'paginas_base/nosotros.html')        

def crear_editarCuota(request,idCuota=0):
      if request.method=="GET":
        if idCuota==0:
            formulario=CuotaForm()   
        else:
            cuotaid=Cuota.objects.get(pk=idCuota)
            formulario=CuotaForm(instance=cuotaid)
        return render(request,'crudCuotas/Crear.html',{'formulario':formulario})
      else:
        if idCuota==0:
            formulario=CuotaForm(request.POST or None, request.FILES or None)
        else:
            cuotaid=Cuota.objects.get(pk=idCuota)
            formulario=CuotaForm(request.POST or None, request.FILES or None ,instance=cuotaid)            
        if formulario.is_valid():
            formulario.save()
        return redirect('listaCuota')
        
def eliminaCuota(request, idCuota):
    bc=Cuota.objects.get(pk=idCuota)
    bc.delete()
    return redirect('listaCuota')
        