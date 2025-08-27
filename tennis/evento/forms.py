from django import forms  # Importa la librería de formularios de Django
from django.core.exceptions import ValidationError   # Para manejar validaciones personalizadas
from .models import Evento, Organizador # Importa los modelos de la app actual
from datetime import datetime # Para trabajar con fechas


from django import forms
from .models import Evento
# Formulario para el modelo Evento
class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento # Se vincula con el modelo Evento
        fields = '__all__' # Incluye todos los campos del modelo
        widgets = {  # Personaliza la apariencia de los campos en el formulario
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del evento'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del evento'}),
            'fecha': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            ),
            'fecha_fin': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            ),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lugar del evento'}),
            'capacidad_max': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad máxima de asistentes'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'idOrganizador': forms.Select(attrs={'class': 'form-control'}),
            'costo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Costo en ARS'}),
        }
        labels = { # Etiquetas personalizadas para cada campo
            'nom': 'Nombre del Evento',
            'descripcion': 'Descripción',
            'fecha': 'Fecha de Inicio',
            'fecha_fin': 'Fecha de Fin',
            'ubicacion': 'Ubicación',
            'capacidad_max': 'Capacidad Máxima',
            'tipo': 'Tipo de Evento',
            'estado': 'Estado del Evento',
            'idOrganizador': 'Organizador',
            'costo': 'Costo (ARS)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # Inicializa el formulario normalmente
        # Ajusta los formatos de fecha para edición
        self.fields['fecha'].input_formats = ['%Y-%m-%dT%H:%M']
        self.fields['fecha_fin'].input_formats = ['%Y-%m-%dT%H:%M']
       # Configura el campo costo como localizable
        self.fields['costo'].localize = True
        self.fields['costo'].widget.is_localized = True

    def clean_fecha(self): # Valida el campo fecha
        fecha = self.cleaned_data['fecha']
        if isinstance(fecha, datetime): # Si ya es un objeto datetime lo retorna
            return fecha
        # Si es solo fecha, lo convierte a datetime con hora mínima
        return datetime.combine(fecha, datetime.min.time())

    def clean_costo(self): # Valida el campo costo
        costo = self.cleaned_data.get("costo")
        if costo is None: # Si no se ingresó, devuelve 0
            return 0
        return round(float(costo), 2) # Redondea a 2 decimales

# Formulario para el modelo Organizador
class OrganizadorForm(forms.ModelForm):
    class Meta:
        model = Organizador  # Se vincula con el modelo Organizador
        fields = ('idOrganizador', 'nom', 'contacto')
        labels = { # Etiquetas personalizadas
            "idOrganizador": "Código del Organizador",
            "nom": "Nombre del Organizador",
            "contacto": "Contacto",
        }

    def __init__(self, *args, **kwargs):
        super(OrganizadorForm, self).__init__(*args, **kwargs)
         # Texto por defecto cuando el campo está vacío
        self.fields['nom'].empty_label = "Selecciona"