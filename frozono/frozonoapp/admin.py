# Register your models here.
from django.contrib import admin
from .models import Categoria
from .models import Producto
from .models import CarritoCompra
from .models import Resena 

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(CarritoCompra)
admin.site.register(Resena)
