from django import forms 
from .models import Servicio, Contratacion

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ('descripcion', 'costo')
        labels = {
            
            'descripcion': 'Descripción:',
            'costo': 'Costo',
        }

    def __init__(self, *args, **kwargs):
        super(ServicioForm, self).__init__(*args, **kwargs)
        
        self.fields['descripcion'].required = True
        self.fields['costo'].required = False


class ContratacionForm(forms.ModelForm):
    servicios = forms.ModelMultipleChoiceField(
        queryset=Servicio.objects.all(),
        required=False
    )
    class Meta:
        model = Contratacion
        fields = ('fecha', 'servicios', 'nomContratante')
        labels = {
            
            'fecha': 'Fecha contratación:',
            'servicios': 'Servicios contratados:',
            'nomContratante': 'Nombre del Contratante',
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'servicios': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ContratacionForm, self).__init__(*args, **kwargs)
        self.fields['fecha'].required = True
        self.fields['nomContratante'].required = False
        self.fields['servicios'].queryset = Servicio.objects.all()
        self.fields['servicios'].empty_label = "Seleccione"