from django.shortcuts import render
from .models import Producto

# Create your views here.
def home(request):
    return render(request, 'app/home.html', {})

def contacto(request):
    return render(request, 'app/contacto.html', {})

def catalogo(request):
    return render(request, 'app/catalogo.html', {})

def login(request):
    return render(request, 'app/login.html', {})

def productdetail(request):
    return render(request, 'app/productdetail.html', {})

def registro(request):
    return render(request, 'app/registro.html', {})

def aboutus(request):
    return render(request, 'app/aboutus.html', {})