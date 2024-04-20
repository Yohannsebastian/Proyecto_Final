from django.shortcuts import render

# Create your views here.
def Porsche(request):
    return render(request, 'Porsche.html')

def Nissan(request):
    return render(request, 'Nissan.html')

def Toyota(request):
    return render(request, 'Toyota.html')

def Mazda(request):
    return render(request, 'Mazda.html')