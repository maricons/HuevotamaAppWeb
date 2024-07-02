"""
URL configuration for frozono project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views
from app.views import ProductoListView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('app/contacto.html', views.contacto, name='contacto'),
    path('app/catalogo.html', views.catalogo, name='catalogo'),
    path('app/login.html', views.login, name='login'),
    path('app/productdetail.html', views.productdetail, name='productdetail'),
    path('app/registro.html', views.registro, name='registro'),
    path('app/aboutus.html', views.aboutus, name='aboutus'),
    path('app/producto_list.html', views.producto_list_html, name='producto_list_html'),
    path('app/', ProductoListView.as_view(), name='producto_list'),  # Ruta para listar productos
    path('app/create/', ProductoCreateView.as_view(), name='producto_create'),  # Ruta para crear producto
    path('app/update/<int:pk>/', ProductoUpdateView.as_view(), name='producto_update'),  # Ruta para actualizar producto
    path('app/delete/<int:pk>/', ProductoDeleteView.as_view(), name='producto_delete'),  # Ruta para eliminar producto
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile_view, name='profile'),
    path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='app/contacto.html'), name='logout'),
    path('salir', views.salir, name='salir')
    # Rutas para categorías (descomentar y ajustar según necesidad)
    # path('categorias/', CategoriaListView.as_view(), name='categoria_list'),
    # path('categorias/create/', CategoriaCreateView.as_view(), name='categoria_create'),
    # path('categorias/update/<int:pk>/', CategoriaUpdateView.as_view(), name='categoria_update'),
    # path('categorias/delete/<int:pk>/', CategoriaDeleteView.as_view(), name='categoria_delete'),
]

