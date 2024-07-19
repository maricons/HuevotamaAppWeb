from django.conf import settings
from .models import Cart, CartItem, Producto

def get_or_create_cart(user):
    """Obtiene el carrito del usuario o crea uno nuevo si no existe."""
    cart, created = Cart.objects.get_or_create(usuario=user)
    return cart

def add_to_cart(user, producto_id, cantidad=1):
    """Agrega un producto al carrito del usuario."""
    cart = get_or_create_cart(user)
    producto = Producto.objects.get(id=producto_id)
    
    # Verifica si el producto ya está en el carrito
    cart_item, created = CartItem.objects.get_or_create(cart=cart, producto=producto)
    
    if not created:
        # Si el artículo ya existe, actualiza la cantidad
        cart_item.cantidad += cantidad
        cart_item.save()
    else:
        # Si el artículo es nuevo, establece la cantidad
        cart_item.cantidad = cantidad
        cart_item.save()

def remove_from_cart(user, producto_id):
    """Elimina un producto del carrito del usuario."""
    cart = get_or_create_cart(user)
    producto = Producto.objects.get(id=producto_id)
    
    # Encuentra y elimina el artículo del carrito
    CartItem.objects.filter(cart=cart, producto=producto).delete()

def update_cart_item(user, producto_id, cantidad):
    """Actualiza la cantidad de un producto en el carrito del usuario."""
    cart = get_or_create_cart(user)
    producto = Producto.objects.get(id=producto_id)
    
    # Encuentra el artículo en el carrito y actualiza la cantidad
    cart_item = CartItem.objects.get(cart=cart, producto=producto)
    cart_item.cantidad = cantidad
    cart_item.save()

def get_cart_items(user):
    """Obtiene todos los artículos del carrito del usuario."""
    cart = get_or_create_cart(user)
    return cart.items.all()

def get_cart_total(user):
    """Calcula el total del carrito del usuario."""
    cart = get_or_create_cart(user)
    return cart.total()
