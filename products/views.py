from django.shortcuts import render, get_object_or_404
from .models import Product


def search(request):
    template = "products/home.html"
    search = request.GET.get('q', '')
    context = {
        'products': Product.objects.filter(title__icontains=search)
    }
    return render(request, template, context)

def home(request):
    template = "products/home.html"
    context = {
        'products': Product.objects.all()
    }
    return render(request, template, context)


def index(request):
    template = 'products/index.html'
    context = {
        'products': Product.objects.all()
    }
    return render(request, template, context)

def show(request, slug):
    template = 'products/show.html'
    product = get_object_or_404(Product, slug=slug)
    images = product.productimage_set.all()
    context = {'product': product, 'images': images}
    return render(request, template, context)