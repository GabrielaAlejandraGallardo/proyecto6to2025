from django.shortcuts import render, redirect, get_object_or_404
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.http import HttpResponse
from .models import SociosCuota
from .forms import SocioCuotaForm
from collections import defaultdict
from socios.models import Socio  # Asegúrate de importar tu modelo Socio

from django.db.models import Q
from .models import SociosCuota

from collections import defaultdict
from django.db.models import Q
from django.shortcuts import render


def listaSocioCuota(request):
    query = request.GET.get('q', '').strip()

    # Obtener todos los socios
    socios = Socio.objects.all().order_by('nom')
    if query:
        socios = socios.filter(nom__icontains=query)

    # Obtener todas las cuotas pagadas
    cuotas_pagadas = SociosCuota.objects.all()

    # Agrupar cuotas por mes
    cuotas_por_mes = defaultdict(list)
    for cuota in cuotas_pagadas:
        cuotas_por_mes[cuota.cuotaMes].append(cuota)

    # Para cada mes, crear lista de socios con estado
    meses = sorted(cuotas_por_mes.keys())
    if not meses:
        # Si no hay cuotas, obtener meses únicos de cuotas existentes o usar un mes por defecto
        meses = list(set(cuota.cuotaMes for cuota in SociosCuota.objects.all()))
        if not meses:
            meses = []  # O manejar caso sin cuotas

    pagos_y_totales = []
    for mes in meses:
        lista_socios = []
        total_mes = 0.0
        for socio in socios:
            # Verificar si el socio pagó en este mes
            pago = next((c for c in cuotas_por_mes[mes] if c.id == socio), None)
            if pago:
                estado = "Al día"
                importe = pago.importe
                fechap = pago.fechap
                cuota_id = pago.idCuota
                total_mes += float(importe or 0)
            else:
                estado = "Debe cuota"
                importe = None
                fechap = None
                cuota_id = None
            lista_socios.append({
                'id': socio.id,
                'nom': socio.nom,
                'estado': estado,
                'importe': importe,
                'fechap': fechap,
                'telefono': socio.tel,
                'cuota_id': cuota_id,
            })
        pagos_y_totales.append((mes, lista_socios, total_mes))

    return render(
        request,
        'CrudSocioCuota/listado.html',
        {'pagos_y_totales': pagos_y_totales, 'query': query}
    )
def inicio(request):
    return render(request,'paginas_base/inicio.html')

def nosotros(request):
    return render(request,'paginas_base/nosotros.html')        

"""def crear_editarSocioCuota(request,id=0):
      if request.method=="GET":
        if id==0:
            formulario=SocioCuotaForm()   
        else:
            Socioid=SociosCuota.objects.get(pk=id)
            formulario=SocioCuotaForm(instance=Socioid)
        return render(request,'CrudSocioCuota/Crear.html',{'formulario':formulario})
      else:
        if id==0:
            formulario=SocioCuotaForm(request.POST or None, request.FILES or None)
        else:
            Socioid=SociosCuota.objects.get(pk=id)
            formulario=SocioCuotaForm(request.POST or None, request.FILES or None ,instance=Socioid)            
        if formulario.is_valid():
            formulario.save()
        return redirect('listaSocioCuota')
    
def crear_editarSocioCuota(request, id=0):
    if request.method == "GET":
        if id == 0:
            formulario = SocioCuotaForm()
        else:
            Socioid = get_object_or_404(SociosCuota, pk=id)
            formulario = SocioCuotaForm(instance=Socioid)
        return render(request, 'CrudSocioCuota/Crear.html', {'formulario': formulario})
    else:
        if id == 0:
            formulario = SocioCuotaForm(request.POST or None, request.FILES or None)
        else:
            Socioid = get_object_or_404(SociosCuota, pk=id)
            formulario = SocioCuotaForm(request.POST or None, request.FILES or None, instance=Socioid)
        if formulario.is_valid():
            formulario.save()
        return redirect('listaSocioCuota')\"\"\"sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        

def crear_editarSocioCuota(request, id=0):
    socios = Socio.objects.all()
    if request.method == "GET":
        if id == 0:
            formulario = SocioCuotaForm()
        else:
            Socioid = get_object_or_404(SociosCuota, pk=id)
            formulario = SocioCuotaForm(instance=Socioid)
        return render(request, 'CrudSocioCuota/Crear.html', {
            'formulario': formulario,
            'socios': socios,  # <-- pasa la lista de socios aquí
        })
    else:
        if id == 0:
            formulario = SocioCuotaForm(request.POST or None, request.FILES or None)
        else:
            Socioid = get_object_or_404(SociosCuota, pk=id)
            formulario = SocioCuotaForm(request.POST or None, request.FILES or None, instance=Socioid)
        if formulario.is_valid():
            formulario.save()
        return redirect('listaSocioCuota')


def eliminarCuotaSocio(request, id):
    bsc = get_object_or_404(SociosCuota, pk=id)
    bsc.delete()
    return redirect('listaSocioCuota')