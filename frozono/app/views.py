from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria
from django.views.generic import View 
from .forms import ProductoForm, CategoriaForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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


@login_required
def producto_list_html(request):
    return render(request, 'app/producto_list.html', {})
    

class ProductoListView(View):
    def get(self, request):
        productos = Producto.objects.all()
        form = ProductoForm
        return render(request, 'app/producto_list.html', {'productos': productos, 'form': form})

class ProductoCreateView(View):
    def post(self, request):
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
        return render(request, 'app/producto_list.html', {'form': form, 'productos': Producto.objects.all()})

class ProductoUpdateView(View):
    def post(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
        return render(request, 'app/producto_list.html', {'form': form, 'productos': Producto.objects.all()})

class ProductoDeleteView(View):
    def post(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        producto.delete()
        return redirect('producto_list')

#class CategoriaListView(View):
 #   def get(self, request):
  #      categorias = Categoria.objects.all()
   #     form = CategoriaForm()
    #    return render(request, 'categorias/categoria_list.html', {'categorias': categorias, 'form': form})

#class CategoriaCreateView(View):
 #   def post(self, request):
  #      form = CategoriaForm(request.POST)
   #     if form.is_valid():
    #        form.save()
     #       return redirect('categoria_list')
      #  return render(request, 'categorias/categoria_list.html', {'form': form, 'categorias': Categoria.objects.all()})

#class CategoriaUpdateView(View):
 #   def post(self, request, pk):
  #      categoria = get_object_or_404(Categoria, pk=pk)
   #     form = CategoriaForm(request.POST, instance=categoria)
    #    if form.is_valid():
     #       form.save()
      #      return redirect('categoria_list')
       # return render(request, 'categorias/categoria_list.html', {'form': form, 'categorias': Categoria.objects.all()})

#class CategoriaDeleteView(View):
 #   def post(self, request, pk):
  #      categoria = get_object_or_404(Categoria, pk=pk)
   #     categoria.delete()
    #    return redirect('categoria_list')

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

def salir(request):
    logout(request)
    return redirect('/')