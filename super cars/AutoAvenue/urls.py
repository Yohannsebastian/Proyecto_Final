
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Inicio.urls')),
    path('Carro/', include('Carro.urls')),
    path('Motor/', include('Motor.urls')),

]
