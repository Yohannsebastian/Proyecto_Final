from django.urls import path
from . import views

urlpatterns = [
    path('motor_porsche/', views.motor_P , name ='motor_porsche'),
    path('Carroceria/', views.Carroceria_1, name = 'Carroceria_1' ),
    path('motor_nissan/', views.motor_N, name = 'motor_nissan'),
    path('carroceria_nissan/', views.carroceria_n, name = 'carroceria_nissan'),
    path('motor_mazda/', views.motro_M, name = 'motor_mazda'),
    path('carroceria_M/', views.carroceria_M , name = 'carroceria_M'),
    path('motor_T/', views.motor_T, name = 'motor_T'),
    path('carroceria_t/', views.carroceria_t, name = 'carroceria_t')
]
