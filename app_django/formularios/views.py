from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def home(request):
    return render(request,'home.html')

def processa_formulario(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    texto = request.POST.get('texto')
    return HttpResponse(f"O nome que você cadastrou é {nome},<br><br> seu e-mail cadastrado é {email}, <br><br> e você deixou a seguinte mensagem: {texto}")
    
