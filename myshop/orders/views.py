from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCraeteForm
from cart.cart import Cart
#from .tasks import order_created

# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCraeteForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'], quantity=item['quantity'])
            cart.clear()
            # запуск асинхронной задачи
            #order_created.delay(order.id)
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCraeteForm
    return render(request, 'orders/order/created.html',
                  {'cart':cart, 'form':form})

