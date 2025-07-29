from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('jugadores/nosotros',views.nosotros,name='nosotros'),
    path('jugadores/lista',views.lista,name='lista'),
    path('jugadores/<int:id>/',views.crear_editarJugador,name='crear_editarJugador'),
    path('jugadores/eliminar/<int:id>',views.eliminar,name='eliminar'),
    path('jugadores/buscar_por_qr', views.buscar_por_qr, name='buscar_por_qr'),
    path('jugadores/descargar_qr_pdf', views.descargar_qr_pdf, name='descargar_qr_pdf'),
    path('scan_qr/', views.pagina_scanner, name='pagina_scanner'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)