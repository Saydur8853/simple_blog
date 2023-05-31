from django.shortcuts import render
from .models import Product


def category_page(request):
    products = Product.objects.all()
    return render(request, "category_page.html", {"products": products})
