from collections import defaultdict
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .forms import CuotaForm
from cuota.models import Cuota
from jugadores.models import Jugador


# Create your views here

def listaCuota(request):
    query = request.GET.get('q', '').strip()

    # Inicialización por defecto para evitar UnboundLocalError
    pagos_por_mes = defaultdict(list)
    total_por_mes = defaultdict(float)

    cuotas = Cuota.objects.all().order_by('cuotaMes')
    if query:
        cuotas = cuotas.filter(nom__icontains=query)
        for sc in cuotas:
            mes = sc.cuotaMes
            pagos_por_mes[mes].append(sc)
            total_por_mes[mes] += float(sc.importe or 0)

    # Construcción de la lista de resultados, incluso si no hay query
    pagos_y_totales = [
        (mes, pagos_por_mes[mes], total_por_mes[mes])
        for mes in pagos_por_mes
    ]

    return render(
        request,
        'CrudCuotas/listado.html',
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
        