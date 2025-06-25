from . import views
from django.urls import path

urlpatterns = [
    ('', views.index, name='index'),
    
]
