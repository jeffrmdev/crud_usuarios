from django.shortcuts import render, redirect
from .models import Persona


# Create your views here.
def home(request):
    lista_personas = Persona.objects.all()
    return render(request, "lista_usuarios.html", {'personas': lista_personas})

def crear(request):
    name = request.POST['name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    cedula = request.POST['cedula']
    phone = request.POST['phone']
    
    persona = Persona.objects.create(
        name = name,
        last_name = last_name,
        email = email,
        cedula = cedula,
        phone = phone
    )
    
    return redirect('/')