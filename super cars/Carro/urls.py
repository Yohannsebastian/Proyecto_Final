from django.urls import path
from . import views

urlpatterns = [
    path('Porsche', views.Porsche , name ='Porsche'),
    path('Nissan', views.Nissan , name = 'Nissan'),
    path('Toyota', views.Toyota, name = 'Toyota'),
    path('Mazda', views.Mazda, name = 'Mazda'),
]