from django.urls import path # Para definir rutas
from . import views # Importa las vistas
from django.conf import settings # Configuración del proyecto
from django.contrib.staticfiles.urls import static  # Para servir archivos estáticos en desarrollo


# Definición de rutas de la aplicación
urlpatterns = [
    path('',views.inicio,name='inicio'), # Página principal
    path('evento/listaEvento',views.listaEvento,name='listaEvento'), # Listado de eventos
    path('evento/crear_editarEvento/<int:idEvento>/', views.crear_editarEvento, name='crear_editarEvento'), # Crear o editar un evento
    path('eliminarEvento/<int:idEvento>/',views.eliminaEvento,name='eliminaEvento'), # Eliminar evento 
    path('evento/listaOrganizador',views.listaOrganizador,name='listaOrganizador'), # Listado de organizadores
    path('evento/crear_editarOrganizador/<int:idOrganizador>/', views.crear_editarOrganizador, name='crear_editarOrganizador'), # 🔹 Ruta para crear o editar un organizador.
# - La URL lleva un parámetro entero <int:idOrganizador>.
#   → Si es 0, se crea un nuevo organizador.
#   → Si existe un ID válido, se edita ese organizador.
# - Llama a la vista "crear_editarOrganizador".
# - El "name" sirve para referenciar esta ruta en plantillas o redirecciones.
    path('eliminarEvento/<int:idOrganizador>/',views.eliminaOrganizador,name='eliminaOrganizador'), # La vista que llama es correcta: "eliminaOrganizador".
# 3. El "name" está bien (eliminaOrganizador), así que lo que confunde es la URL.



      
 
 
 
 
    


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # Esto agrega a urlpatterns la configuración para servir archivos multimedia (imágenes, PDFs, etc.)
# en modo de desarrollo, usando los valores definidos en settings.MEDIA_URL y settings.MEDIA_ROOT.