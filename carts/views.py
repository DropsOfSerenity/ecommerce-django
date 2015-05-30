from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from products.models import Product
from decimal import Decimal
from .models import Cart


def view(request):
    cart = Cart.objects.all()[0]
    context = {'cart': cart}
    template = 'cart/view.html'
    return render(request, template, context)


def update_cart(request, slug):
    cart = Cart.objects.all()[0]
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass
    if product not in cart.products.all():
        cart.products.add(product)
    else:
        cart.products.remove(product)

    new_total = Decimal(0.00)
    for item in cart.products.all():
        new_total += item.price
    cart.total = new_total
    cart.save()

    return HttpResponseRedirect(reverse('cart'))
