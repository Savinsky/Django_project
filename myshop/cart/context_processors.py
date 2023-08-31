from .cart import Cart

def cart(request):
    return {'cart': Cart(request)}

# Контекстный процессор для корзины будет выполняться при каждом просмотре шаблона