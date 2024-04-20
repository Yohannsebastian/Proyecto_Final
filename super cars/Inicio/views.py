from django.shortcuts import render
from django.http import HttpResponse
from .models import Formulario
from .form import Form


# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')


def formulario(request):
    if request.method == 'POST':
      form = Form(request.POST)
      if form.is_valid():
          form.save()
          form = Form()
    else:
        form =Form()
    return render(request, 'Formulario.html',{
        'formulario': form})

def elimina_formulario(request, id):
    formulario = Formulario.objects.get(id=id)
    formulario.delete()
    return HttpResponse('Eliminados exitosamente')