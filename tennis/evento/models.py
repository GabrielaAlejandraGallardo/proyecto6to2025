from django.db import models
#from jugadores.models import Jugador

class Organizador(models.Model):
    idOrganizador=models.AutoField(primary_key=True,verbose_name="idOrganizador",db_column='idOrganizador')
    nom=models.CharField(max_length=45,verbose_name="nombre")
    contacto=models.IntegerField(verbose_name="contacto")
    
    def __str__(self):
        fila=str(self.idOrganizador)+"-Nombre Organizador: "+self.nom+"-Contacto: "+str(self.contacto)
        return fila
    
        # Para almacenar fecha y hora juntos, se puede usar DateTimeField en Django:
      #  fecha_hora = models.DateTimeField(verbose_name="Fecha y Hora", null=True, blank=True)
class Evento(models.Model):
    idEvento=models.AutoField(primary_key=True,verbose_name="idEvento",db_column='idEvento')
    nom= models.CharField(max_length=50,verbose_name="Nombre y Apellido")
    fecha=models.DateTimeField(verbose_name="Fecha de Evento",unique=True)
    ubicacion=models.CharField(max_length=20,verbose_name="Ubicacion")
    idOrganizador=models.ForeignKey(Organizador,verbose_name="idOrganizador", on_delete=models.CASCADE)
    
    def __str__(self):
        fila=str(self.idEvento)+"-"+self.nom+""+str(self.idOrganizador)
        return fila
    
    
    
    
    
    
