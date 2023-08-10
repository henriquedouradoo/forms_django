from django.shortcuts import render
from django.http import HttpResponse 
from .models import Usuarios
# Create your views here.
def home(request):
    return render(request,'home.html')

def processa_formulario(request):
    novo_usuarios = Usuarios()
    novo_usuarios.nome = request.POST.get('nome')
    novo_usuarios.email = request.POST.get('email')
    novo_usuarios.texto = request.POST.get('texto')
    novo_usuarios.save()

    Usuario = {
        'usuarios': Usuarios.objects.all()
    }

    return render(request,'usuarios/usuarios.html',Usuario)
    
    
    
