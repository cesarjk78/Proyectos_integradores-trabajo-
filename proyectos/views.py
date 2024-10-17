from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import ProyectoIntegrador
from django.utils import timezone

def home(request):
    return render(request, 'proyectos/index.html')  # Asegúrate de que la ruta coincida con la ubicación de tu archivo

def quienes_somos(request):
    return render(request, 'proyectos/quienesomos.html') 

#Login

def es_admin(user):
    return user.groups.filter(name='Admin').exists()

def crear_usuario(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

       
        if User.objects.filter(email=email).exists():
            return redirect('registrar')
        else:
         
            user = User.objects.create_user(
                username=email,  
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            user.save()
            return redirect('iniciar_sesion')  

    return render(request, 'proyectos/registrar.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        email = request.POST.get('email') 
        password = request.POST.get('password')

        try:
        
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:8000/')
        else:
            messages.error(request, 'Correo o contraseña incorrectos.')

    return render(request, 'proyectos/iniciar_sesion.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('proyectos/iniciar_sesion.html')


def listar_proyectos(request):
    proyectos = ProyectoIntegrador.objects.all()  # Obtén todos los proyectos
    return render(request, 'proyectos/listar_proyectos.html', {'proyectos': proyectos})