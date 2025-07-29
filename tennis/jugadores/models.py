from django.db import models
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile

class Deporte(models.Model):
    descripcion=models.CharField(max_length=50,verbose_name="descripcion")
    
    def __str__(self):
      fila=self.descripcion
      return fila
class Talla(models.Model):
    talla=models.CharField(max_length=50,verbose_name="talla")
    
    def __str__(self):
      fila=self.talla
      return fila
    
# Create your models here.
class Jugador(models.Model):
  id = models.AutoField(primary_key=True, db_column='id')
  DNI = models.IntegerField(verbose_name="DNI")
  nom = models.CharField(max_length=50, verbose_name="Nombre y Apellido")
  fechan = models.DateField(verbose_name="Fecha Nacimiento")
  altura = models.FloatField(max_length=3, verbose_name="Altura")
  peso = models.FloatField(max_length=3, verbose_name="Peso")
  dire = models.CharField(max_length=50, verbose_name="Direccion")
  cd = models.CharField(max_length=6, verbose_name="codigo postal")
  talla = models.ForeignKey(Talla, verbose_name="talla", on_delete=models.CASCADE)
  descripcion = models.ForeignKey(Deporte, verbose_name="descripcion", on_delete=models.CASCADE)
  qr = models.ImageField(upload_to='jugadores/qr/', blank=True, null=True, verbose_name="QR")
 

  def __str__(self):
    fila = str(self.id) + "-" + str(self.DNI) + "-" + self.nom
    return fila

  def save(self, *args, **kwargs):
    # Generar el contenido del QR (puedes personalizar esto)
    qr_content = f'Jugador: {self.nom}, DNI: {self.DNI}'
    qr_img = qrcode.make(qr_content)
    buffer = BytesIO()
    qr_img.save(buffer, format='PNG')
    file_name = f'qr_{self.DNI}.png'
    self.qr.save(file_name, ContentFile(buffer.getvalue()), save=False)
    super().save(*args, **kwargs)
    


    
















