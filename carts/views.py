from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from products.models import Product
from decimal import Decimal
from .models import Cart


def view(request):
    cart_id = request.session.get('cart_id')
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
        context = {'cart': cart}
    else:
        empty_message = 'You have an empty Cart.'
        context = {'empty': True, 'empty_message': empty_message}
    template = 'cart/view.html'
    return render(request, template, context)


def update_cart(request, slug):
    request.session.set_expiry(120000)
    try:
        cart_id = request.session['cart_id']
    except KeyError:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        cart_id = new_cart.id

    cart = Cart.objects.get(id=cart_id)

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
    request.session['items_total'] = cart.products.count()
    cart.total = new_total
    cart.save()

    return HttpResponseRedirect(reverse('cart'))
