from django.shortcuts import render
from .models import Producto

# Create your views here.
def home(request):
    return render(request, 'app/home.html', {})