from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('socios/nosotros',views.nosotros,name='nosotros'),
    path('socios/listaSocio',views.listaSocio,name='listaSocio'),
    path('socios/crear_editarSocio/<int:id>/',views.crear_editarSocio,name='crear_editarSocio'),
    path('socios/eliminarSO/<int:id>',views.eliminarSO,name='eliminarSO'),
    path('socios/buscar_por_qr', views.buscar_por_qr, name='buscar_por_qr'),
    path('socios/descargar_qr_pdf', views.descargar_qr_pdf, name='descargar_qr_pdf'),
  

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)