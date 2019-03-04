from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def product_new(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'new_product.html', {'form': form})
