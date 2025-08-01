from io import BytesIO
import json
from quopri import decode
from tkinter import Canvas
from tkinter.tix import Meter
from django.shortcuts import render, redirect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.http import FileResponse, HttpResponse, JsonResponse
from .models import Socio
from .forms import SocioForm
from django.core.files.base import ContentFile

# Create your views here
def listaSocio(request):
    socio=Socio.objects.all()
    return render(request,"CrudSocio/listado.html",{'socio':socio})


def inicio(request):
    return render(request,'paginas_base/inicio.html')

def nosotros(request):
    return render(request,'paginas_base/nosotros.html')        

def crear_editarSocio(request,id=0):
      if request.method=="GET":
        if id==0:
            formulario=SocioForm()   
        else:
            Socioid=Socio.objects.get(pk=id)
            formulario=SocioForm(instance=Socioid)
        return render(request,'CrudSocio/Crear.html',{'formulario':formulario})
      else:
        if id==0:
            formulario=SocioForm(request.POST or None, request.FILES or None)
        else:
            Socioid=Socio.objects.get(pk=id)
            formulario=SocioForm(request.POST or None, request.FILES or None ,instance=Socioid)            
        if formulario.is_valid():
            formulario.save()
        return redirect('listaSocio')

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
                socio = Socio.objects.get(qr_code_data=qr_data)
                # Puedes devolver la info del jugador en JSON
                jugador_data = {
                    'DNI': socio.DNI,
                    'Nombre':socio.nom,
                    'Fecha Nacimiento': str(socio.fechan),
                    'dire': socio.dire,
                    'cp': socio.cp,
                    'tel':socio.tel,
                   
                   
                   
                }
                return JsonResponse({'status': 'success', 'jugador': jugador_data})
            except socio.DoesNotExist:
                return JsonResponse({'status': 'not_found'})
        else:
            return JsonResponse({'status': 'error', 'message': 'No QR data provided'})
    # Para otras solicitudes, renderiza la página de escaneo
    return render(request, 'Crud/scan_qr.html')
def crear_editarJugador(request, id=0):
    if request.method == "GET":
        if id == 0:
            formulario = SocioForm()
        else:
            socioid = Socio.objects.get(pk=id)
            formulario = SocioForm(instance=jugadorid)
        return render(request, 'Crud/Crear.html', {'formulario': formulario})
    else:
        if id == 0:
            formulario = SocioForm(request.POST or None, request.FILES or None)
        else:
            jugadorid = Socio.objects.get(pk=id)
            formulario = SocioForm(request.POST or None, request.FILES or None, instance=socioid)   
        if formulario.is_valid():
            socio= formulario.save(commit=False)
            # Generar datos únicos para el QR (puedes usar el ID, nombre, etc.)
            qr_data = (
            f"DNI: {socio.DNI}\n"
            f"Nombre: {socio.nom}\n"
            f"Fecha Nacimiento: {socio.fechan}\n"
            f"Dirección: {socio.dire}\n"
            f"Código Postal: {socio.cp}\n"
            f"Telefono: {socio.tel}\n"
         
             )
            socio.qr_code_data = qr_data  # Asume que tienes este campo en tu modelo
            socio.save()  # Guardar primero para asegurar que el ID existe y qr_code_dat
            # Generar imagen QR
            qr_img = decode.make(qr_data)
            buffer = BytesIO()
            qr_img.save(buffer, format='PNG')
            socio.qr.save(f"qr_{socio.id}.png",ContentFile(buffer.getvalue()), save=False)  # Usar el ID para el nombre del archivo
            socio.save()
        return redirect('lista')

def descargar_qr_pdf(request, id):
    socio= Socio.objects.get(pk=id)
    buffer = BytesIO()
    p = Canvas.Canvas(buffer, pagesize=Meter)
    p.drawString(100, 750, f"QR de {socio.nom}")
    # Insertar imagen QR
    if socio.qr_code:
        p.drawInlineImage(socio.qr_code.path, 100, 600, width=250, height=250)
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f'qr_{socio.nom}.pdf')     
   
def eliminarSO(request, id):
    bc=Socio.objects.get(pk=id)
    bc.delete()
    return redirect('listaSocio')
        