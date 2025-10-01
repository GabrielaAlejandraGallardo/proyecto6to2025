from django.db import models
class Servicio(models.Model):
    idServicio = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.descripcion

class Contratacion(models.Model):
    idContratacion = models.AutoField(primary_key=True)
    fecha = models.DateField()
    nomContratante = models.CharField(max_length=100)
    servicios = models.ManyToManyField(Servicio)
    total_costo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    

    def __str__(self):
        return f"Contratación {self.idContratacion} - {self.nomContratante}"
