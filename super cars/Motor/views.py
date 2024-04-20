from django.shortcuts import render

# Create your views here.
def motor_P(request):
    return render(request, 'Motor_Porsche.html')

def Carroceria_1(request):
    return render(request ,'Carroceria_1.html')

def motor_N(request):
    return render(request,'motor_nissan.html')

def carroceria_n(request):
    return render(request,'carroceria_nissan.html')

def motro_M(request):
    return render(request,'motor_mazda.html')

def carroceria_M(request):
    return render(request,'carroceria_M.html')

def motor_T(request):
    return render(request, 'motor_T.html')

def carroceria_t(requeat):
    return render(requeat,'carroceria_t.html')


