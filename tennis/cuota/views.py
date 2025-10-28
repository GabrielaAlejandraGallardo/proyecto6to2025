from collections import defaultdict
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .forms import CuotaForm
from cuota.models import Cuota
from jugadores.models import Jugador
from django.db.models import Q


# Create your views here

def listaCuota(request):
    query = request.GET.get('q', '').strip()

    # Obtener todos los jugadores
    jugadores = Jugador.objects.all().order_by('nom')
    if query:
        jugadores = jugadores.filter(nom__icontains=query)

    # Obtener todas las cuotas pagadas
    cuotas_pagadas = Cuota.objects.all()

    # Agrupar cuotas por mes
    cuotas_por_mes = defaultdict(list)
    for cuota in cuotas_pagadas:
        cuotas_por_mes[cuota.cuotaMes].append(cuota)

    # Para cada mes, crear lista de jugadores con estado
    meses = sorted(cuotas_por_mes.keys())
    if not meses:
        # Si no hay cuotas, obtener meses únicos de cuotas existentes o usar un mes por defecto
        meses = list(set(cuota.cuotaMes for cuota in Cuota.objects.all()))
        if not meses:
            meses = []  # O manejar caso sin cuotas

    pagos_y_totales = []
    for mes in meses:
        lista_jugadores = []
        total_mes = 0.0
        for jugador in jugadores:
            # Verificar si el jugador pagó en este mes
            pago = next((c for c in cuotas_por_mes[mes] if c.id == jugador), None)
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
            lista_jugadores.append({
                'id': jugador.id,
                'nom': jugador.nom,
                'estado': estado,
                'importe': importe,
                'fechap': fechap,
                'whatsapp': jugador.whatsapp,
                'cuota_id': cuota_id,
            })
        pagos_y_totales.append((mes, lista_jugadores, total_mes))

    return render(
        request,
        'crudCuotas/listado.html',
        {'pagos_y_totales': pagos_y_totales, 'query': query}
    )

    
     

    
    
    


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
        
def obtener_nombre_jugador(request, pk):
    try:
        jugador = Jugador.objects.get(pk=pk)
        return JsonResponse({'nom': jugador.nom})
    except Jugador.DoesNotExist:
        return JsonResponse({'nom': ''}, status=404)        
        