from django.db import models # Importa la librería de modelos de Django
from django.contrib.humanize.templatetags.humanize import intcomma # Para formatear números con comas

# Función para mostrar el costo formateado con comas y decimales
def costo_formateado(self):
    if self.costo is not None: # Si el costo tiene un valor (no está vacío o en NULL)
        # Separamos parte entera y decimal
        entero = int(self.costo)  # Parte entera  # Convierte la parte entera del costo en un número entero.
        decimal = f"{self.costo:.2f}".split(".")[1] # Parte decimal # Convierte el costo a string con 2 decimales, lo separa por el punto,
        # y se queda con la parte decimal.
        return f"ARS {intcomma(entero)},{decimal}"  # Usa "intcomma" para agregar comas a los miles.
        # Ejemplo: 1500 → "1,500"
        # Devuelve algo como: "ARS 1,500,75"
    return "Gratis"    # Si el campo costo está vacío (None), devuelve la palabra "Gratis".

# Modelo Organizador
class Organizador(models.Model):  # Definición del modelo "Organizador", que representa a la persona/entidad que organiza un evento.
    idOrganizador = models.AutoField( # Clave primaria autoincremental (ID único)
        primary_key=True,
        verbose_name="idOrganizador", # Nombre visible en el admin o formularios
        db_column='idOrganizador' # Nombre exacto de la columna en la base de datos
    )
    nom = models.CharField(max_length=45, verbose_name="nombre") # Cadena de texto de hasta 45 caracteres 
    # Nombre del organizador
    contacto = models.IntegerField(verbose_name="contacto") # Campo numérico (generalmente un teléfono o código de contacto)

    def __str__(self): # Representación en texto
        return f"{self.idOrganizador} - {self.nom}"

# Modelo Evento
class Evento(models.Model):
    TIPOS_EVENTO = [ # Opciones de tipos de evento
        ('PEÑA', 'Peña'),
        ('FIESTA', 'Fiesta'),
        ('TORNEO', 'Torneo'),
        ('OTRO', 'Otro'),
    ]

    ESTADOS = [ # Opciones de estado del evento
        ('ACTIVO', 'Activo'),
        ('FINALIZADO', 'Finalizado'),
        ('CANCELADO', 'Cancelado'),
    ]

    idEvento = models.AutoField(
        primary_key=True,
        verbose_name="idEvento",
        db_column='idEvento'
    )
    nom = models.CharField(max_length=50, verbose_name="Nombre del Evento") # Define que es la clave primaria (ID único del evento, autoincremental)
    # Nombre de la columna en la base de datos
    # Nombre que se muestra en el panel de administración 
    # Límite de 50 caracteres para el nombre
    # Etiqueta que se verá en formularios/admin
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción") # Permite que se deje vacío en formularios
    # Permite que en la base de datos quede en NULL
     # Etiqueta del campo
    fecha = models.DateTimeField(verbose_name="Fecha de Inicio") # Campo obligatorio: fecha y hora de inicio
    fecha_fin = models.DateTimeField(blank=True, null=True, verbose_name="Fecha de Fin") # Opcional: puede quedar vacío
    # Fecha y hora de finalización
    ubicacion = models.CharField(max_length=100, verbose_name="Ubicación") # Hasta 100 caracteres para la dirección o lugar
    capacidad_max = models.PositiveIntegerField(blank=True, null=True, verbose_name="Capacidad Máxima") # Campo opcional
    # Número máximo de asistentes permitidos
    tipo = models.CharField(max_length=20, choices=TIPOS_EVENTO, default='OTRO')# Guarda un texto de hasta 20 caracteres
     # Se restringe a las opciones definidas en TIPOS_EVENTO
     # Valor por defecto
    estado = models.CharField(max_length=20, choices=ESTADOS, default='ACTIVO') # Hasta 20 caracteres
    # Se restringe a las opciones definidas en ESTADOS
     # Valor por defecto
    costo = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, verbose_name="Costo") # Hasta 8 dígitos en total (ej: 999999.99)
    # Se permiten 2 decimales (ej: 150.50)
    # Puede dejarse vacío
    # Etiqueta en formularios/admin
    idOrganizador = models.ForeignKey(
        Organizador, # Relación con el modelo Organizador
        verbose_name="Organizador", # Nombre visible
        on_delete=models.CASCADE # Si se elimina el organizador, también se eliminan sus eventos
    )
     # Método que define cómo se muestra el objeto en el admin o en representaciones de texto
    def __str__(self):
        return f"{self.idEvento} - {self.nom}"
    
    def costo_formateado(self): # Devuelve el costo con formato
        if self.costo is not None:
            # Separamos entero y decimales
            entero = int(self.costo)
            decimal = f"{self.costo:.2f}".split(".")[1]
            return f"ARS {intcomma(entero)},{decimal}"
        return "Gratis"