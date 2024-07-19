from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria, Cart, CartItem
from django.contrib.auth.decorators import login_required

from .forms import ProductoForm, CategoriaForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
def home(request):
    productos = Producto.objects.all()
    return render(request, 'app/home.html', {'object_list': productos})

def productlist(request):
    productos = Producto.objects.all()
    return render(request, 'app/productlist.html',  {'object_list': productos})

class ProductCreateView(CreateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio', 'categoria', 'stock']
    template_name = 'app/productcreate.html'
    success_url = '/app/productlist.html' # Redirige a la lista de productos después de crear uno nuevo

class ProductUpdateView(UpdateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio', 'categoria', 'stock']
    template_name = 'app/productedit.html'
    success_url = '/app/productlist.html' # Redirige a la lista de productos después de crear uno nuevo

class ProductDeleteView(DeleteView):
    model = Producto
    success_url = '/app/productlist.html' # Redirige a la lista de productos después de crear uno nuevo   

class ProductListView(CreateView):
    model = Producto

def contacto(request):
    return render(request, 'app/contacto.html', {})

def catalogo(request):
    productos = Producto.objects.all( )
    return render(request, 'app/catalogo.html', {'object_list': productos})

def login(request):
    return render(request, 'app/login.html', {})

def productdetail(request):
    return render(request, 'app/productdetail.html', {})

def registro(request):
    return render(request, 'app/registro.html', {})

def aboutus(request):
    return render(request, 'app/aboutus.html', {})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['user']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Mostrar mensaje de alerta de inicio de sesión exitoso
                return render(request, 'login.html', {'form': form, 'alert_success': True})
            else:
                return render(request, 'login.html', {'form': form, 'error_message': 'Credenciales inválidas.'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def profile_view(request):
    # Obtener el usuario actual
    user = request.user

    # Aquí puedes agregar lógica para obtener otros datos del perfil del usuario
    # Por ejemplo, obtener datos adicionales del modelo UserProfile si lo tienes

    # Renderizar el template del perfil con los datos del usuario
    return render(request, 'app/profile.html', {'user': user})    