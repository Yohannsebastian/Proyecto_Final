from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('formulario/', views.formulario, name = 'Formulario'),
    path('eliminar/<int:id>', views.elimina_formulario, name='eliminar_formulario')
]