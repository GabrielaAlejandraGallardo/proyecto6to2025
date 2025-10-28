from django import forms
from .models import SociosCuota

class SocioCuotaForm(forms.ModelForm):
  class Meta:
        model=SociosCuota
       #fields='__all__'
        fields=('idCuota','id','nom','cuotaMes','fechap',"importe")
        labels ={
          
            "idCuota":" id cuota",
            "id" : "Socio" ,
            'nom': 'nombre y apellido del jugador',
            "cuotaMes":"Mes al que corresponde la cuota",
            "fechap" : "fecha de pago" ,
            "importe" : "valor cuota" ,

          #  "nummac" : "numero de macc " ,
           
                   
        
        }
        
        widgets = {
        "cuotaMes": forms.DateInput(attrs={'type': 'date'}),
        'fechap': forms.DateInput(attrs={'type': 'date'}),
        }
        
  def __init__(self, *args, **kwargs):
    super(SocioCuotaForm, self).__init__(*args, **kwargs)
    self.fields['nom'].required = True
    self.fields['fechap'].required = False