# Register your models here.
from django.contrib import admin
from .models import Categoria
from .models import Producto
from .models import Cart
from .models import CartItem

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cart)
admin.site.register(CartItem)