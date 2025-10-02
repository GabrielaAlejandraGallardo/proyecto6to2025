from django.shortcuts import render, redirect
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.http import HttpResponse
from .models import Jugador
from .forms import JugadorForm
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.http import FileResponse
import json
from django.http import JsonResponse

# Create your views here

def lista(request):
    jugadores=Jugador.objects.all()
    
    return render(request,"Crud/listado.html",{'jugadores':jugadores})


def inicio(request):
    return render(request,'paginas_base/inicio.html')

def nosotros(request):
    return render(request,'paginas_base/nosotros.html')        


def buscar_por_qr(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            qr_data = body.get('qr_data')
        except json.JSONDecodeError:
            qr_data = request.POST.get('qr_data')
        jugador = None
        if qr_data:
            try:
                jugador = Jugador.objects.get(qr_code_data=qr_data)
                # Puedes devolver la info del jugador en JSON
                jugador_data = {
                    'DNI': jugador.DNI,
                    'Nombre': jugador.nom,
                    'Fecha Nacimiento': str(jugador.fechan),
                    'Altura': jugador.altura,
                    'Peso': jugador.peso,
                    'Dirección': jugador.dire,
                    'Código Postal': jugador.cd,
                    'Talla': jugador.talla,
                    'Deporte': jugador.descripcion,
                    'cuota': jugador.idCuota.nom,
                }
                return JsonResponse({'status': 'success', 'jugador': jugador_data})
            except Jugador.DoesNotExist:
                return JsonResponse({'status': 'not_found'})
        else:
            return JsonResponse({'status': 'error', 'message': 'No QR data provided'})
    # Para otras solicitudes, renderiza la página de escaneo
    return render(request, 'Crud/scan_qr.html')
def crear_editarJugador(request, id=0):
    if request.method == "GET":
        if id == 0:
            formulario = JugadorForm()
        else:
            jugadorid = Jugador.objects.get(pk=id)
            formulario = JugadorForm(instance=jugadorid)
        return render(request, 'Crud/Crear.html', {'formulario': formulario})
    else:
        if id == 0:
            formulario = JugadorForm(request.POST or None, request.FILES or None)
        else:
            jugadorid = Jugador.objects.get(pk=id)
            formulario = JugadorForm(request.POST or None, request.FILES or None, instance=jugadorid)
        if formulario.is_valid():
            jugador = formulario.save(commit=False)
            # Generar datos únicos para el QR (puedes usar el ID, nombre, etc.)
            qr_data = (
            f"DNI: {jugador.DNI}\n"
            f"Nombre: {jugador.nom}\n"
            f"Fecha Nacimiento: {jugador.fechan}\n"
            f"Altura: {jugador.altura}\n"
            f"Peso: {jugador.peso}\n"
            f"Dirección: {jugador.dire}\n"
            f"Código Postal: {jugador.cd}\n"
            f"Talla: {jugador.talla}\n"
            f"Deporte: {jugador.descripcion}\n"
            f"Cuota: {jugador.idCuota.nom}\n"
             )
            jugador.qr_code_data = qr_data  # Asume que tienes este campo en tu modelo
            jugador.save()  # Guardar primero para asegurar que el ID existe y qr_code_data
            # Generar imagen QR
            qr_img = qrcode.make(qr_data)
            buffer = BytesIO()
            qr_img.save(buffer, format='PNG')
            jugador.qr.save(f"qr_{jugador.id}.png", ContentFile(buffer.getvalue()), save=False)  # Usar el ID para el nombre del archivo
            jugador.save()
        return redirect('lista')
    
def eliminar(request, id):
    bc=Jugador.objects.get(pk=id)
    bc.delete()
    return redirect('lista')
def pagina_scanner(request):
    return render(request, 'CrudSocio/scan_qr.html')        