from django import forms
from django.forms import SelectMultiple
from .models import Servicio, Contratacion

class ServicioForm(forms.ModelForm):
 class Meta:
  model = Servicio
  fields = ('descripcion', 'costo')
  labels = {
'descripcion': 'Descripción:',
'costo': 'Costo',
}

def init(self, *args, **kwargs):
 super(ServicioForm, self).init(*args, **kwargs)
 self.fields['descripcion'].empty_label = "Selecciona"
 self.fields['descripcion'].required = True
 self.fields['costo'].required = False

class ContratacionForm(forms.ModelForm):
  class Meta:
   model = Contratacion
   fields = ('fecha', 'idServicio', 'servicios', 'nomContratante')
   labels = {
'fecha': 'Fecha contratación:',
'idServicio': 'Cód de Servicio',
'servicios': 'Servicios',
'nomContratante': 'Nombre del Contratante',
}
   widgets = {
'fecha': forms.DateInput(attrs={'type': 'date'}),
'servicios': SelectMultiple(attrs={'size': 6}),
}

def init(self, *args, **kwargs):
 super(ContratacionForm, self).init(*args, **kwargs)
 self.fields['idServicio'].required = True
 self.fields['servicios'].required = True # obligatorio si quieres al menos un servicio
 self.fields['fecha'].required = True
 self.fields['nomContratante'].required = False

def clean_servicios(self):
 servicios = self.cleaned_data.get('servicios')
 if not servicios or len(servicios) == 0:
    raise forms.ValidationError("Debe seleccionar al menos un servicio.")
 return servicios









      
   


