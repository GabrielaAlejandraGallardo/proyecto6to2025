from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static



urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('cuota/listaCuota',views.listaCuota,name='listaCuota'),
    path('<int:idCuota>/', views.crear_editarCuota, name='crear_editarCuota'),
    path('eliminarCuota/<int:idCuota>/',views.eliminaCuota,name='eliminaCuota'),  
     path('api/jugador/<int:pk>/nom/', views.obtener_nombre_jugador, name='obtener_nombre_jugador'),
     path('cuota/', views.listaCuota, name='listaCuota'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)