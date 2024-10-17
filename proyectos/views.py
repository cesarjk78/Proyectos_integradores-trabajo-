from django.shortcuts import render

def home(request):
    return render(request, 'proyectos/index.html')  # Asegúrate de que la ruta coincida con la ubicación de tu archivo

def quienes_somos(request):
    return render(request, 'proyectos/quienesomos.html') 
