from django.shortcuts import render, redirect # Funciones para renderizar plantillas y redirigir
from django.http import HttpResponse # Para respuestas HTTP simples
from crispy_forms.helper import FormHelper  # Para mejorar formularios con Crispy Forms
from crispy_forms.layout import Submit # Importa la clase "Submit" de Crispy Forms, que sirve para agregar botones de envío a los formularios
# (en este caso no se está usando en el modelo, probablemente se usará en los formularios)
from .forms import EventoForm, OrganizadorForm # Formularios de la app
from evento.models import Evento, Organizador # Modelos de la app

# Create your views here
# Vista para listar eventos
def listaEvento(request): # Vista que muestra la lista de todos los eventos guardados en la base de datos.
    eventos=Evento.objects.all() # Obtiene todos los registros del modelo Evento.
    # Esto devuelve un QuerySet con todos los eventos.
    return render(request,"crudEvento/listado.html",# Plantilla HTML que va a renderizarse
                  {'eventos':eventos})# Contexto: se envía la lista de eventos a la plantilla bajo la clave 'eventos'

# Vista de inicio
def inicio(request): # Vista de la página principal (inicio).
    return render(request,'paginas_base/inicio.html') # Renderiza directamente la plantilla de inicio
# Vista "nosotros"
def nosotros(request):
    return render(request,'paginas_base/nosotros.html')        
# Crear o editar un evento
def crear_editarEvento(request,idEvento=0):# Vista para crear un nuevo evento o editar uno existente.
    # Recibe como parámetro el idEvento. Si es 0 → crear, si no → editar.
      if request.method=="GET":# CREA UN FORMULARIO VACIO # Si es GET → muestra el formulario vacío o con datos
        if idEvento==0:  # Si idEvento es 0 → significa que es un nuevo evento.
            # Se crea un formulario vacío para que el usuario lo complete.
            formulario=EventoForm()   # Crear evento
        else: # Si es POST → guarda los datos
            eventoid=Evento.objects.get(pk=idEvento) # Si idEvento no es 0 → significa que el usuario quiere editar un evento existente.
            # Se busca ese evento en la base de datos.
            formulario=EventoForm(instance=eventoid) # Se carga el formulario con los datos del evento encontrado, para mostrarlos al usuario.
        return render(request,'crudEvento/Crear.html',# Plantilla donde se mostrará el formulario
                      {'formulario':formulario}) # Se pasa el formulario al template
      else:#, se busca el evento existente y se vincula al formulario con los datos enviados.

        if idEvento==0:#Si idEvento es 0, se crea un formulario con los datos enviados (request.POST y request.FILES).
            formulario=EventoForm(request.POST or None, request.FILES or None)
        else: 
            eventoid=Evento.objects.get(pk=idEvento)  # Si el idEvento existe, se busca el evento correspondiente.
            formulario=EventoForm(request.POST or None, request.FILES or None ,instance=eventoid)   # Se carga el formulario con los datos enviados, pero vinculado al evento existente,
            # de manera que al guardar se actualice en vez de crear uno nuevo.          
        if formulario.is_valid():  # Si todos los datos son válidos (pasan las validaciones de Django y las personalizadas)
            formulario.save()  # Guarda el evento (ya sea nuevo o editado)
        return redirect('listaEvento') # Redirige al listado # Redirige a la vista de listado de eventos, para mostrar los cambios.
# Eliminar evento        
def eliminaEvento(request, idEvento): 
    bc=Evento.objects.get(pk=idEvento) # Busca evento por ID
    bc.delete() # Lo elimina
    return redirect('listaEvento')
        
# Listar organizadores
def listaOrganizador(request):  # Vista que muestra todos los organizadores guardados en la base de datos.
    organizadores=Evento.objects.all()
    return render(request,"crudEvento/listado.html",# Plantilla donde se mostrará la lista
                  {'organizadores':organizadores}) # Se pasa la lista al template con la clave 'organizadores'

 
# Crear o editar un organizador
def crear_editarOrganizador(request,idOrganizador=0):
      if request.method=="GET":# CREA UN FORMULARIO VACIO
        if idOrganizador==0:
            formulario=OrganizadorForm()   # Crear organizador
        else:
            organizadorid=Organizador.objects.get(pk=idOrganizador)
            formulario=OrganizadorForm(instance=organizadorid)
        return render(request,'crudEOrganizador/Crear.html',{'formulario':formulario})
      else:#, se busca el evento existente y se vincula al formulario con los datos enviados.

        if idOrganizador==0:#Si idEvento es 0, se crea un formulario con los datos enviados (request.POST y request.FILES).
            formulario=OrganizadorForm(request.POST or None, request.FILES or None)
        else:
            organizadorid=Organizador.objects.get(pk=idOrganizador)
            formulario=OrganizadorForm(request.POST or None, request.FILES or None ,instance=organizadorid)            
        if formulario.is_valid():
            formulario.save()
        return redirect('listaOrganizador')
# Eliminar organizador        
def eliminaOrganizador(request, idOrganizador): # Vista que elimina un organizador de la base de datos.
    # Recibe como parámetro el ID del organizador que se quiere eliminar.
    bc=Organizador.objects.get(pk=idOrganizador)  # Busca en la base de datos el organizador cuyo idOrganizador coincide con el recibido.
    # Si no lo encuentra, Django lanzará un error "DoesNotExist".
    bc.delete() # Elimina ese organizador de la base de datos de forma permanente.
    return redirect('listaEOrganizador')   # Redirige al usuario a la vista que lista los organizadores.        