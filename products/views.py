from django.shortcuts import render
from django.db.models import Max
from .models import Product, Category, Brand, Warranty, Seller, BannerImage


def products_page(request):
    banner_image = BannerImage.objects.latest("pk")
    products = Product.objects.all()
    highest_price = products.aggregate(Max("price"))["price__max"]
    categories = Category.objects.all()
    brands = Brand.objects.all()
    warranties = Warranty.objects.all()
    sellers = Seller.objects.all()

    # Get highest price
    highest_price = products.aggregate(Max("price"))["price__max"]

    # Apply filters
    price_filter = request.GET.get("price")
    category_filter = request.GET.get("category")
    brand_filter = request.GET.get("brand")
    warranty_filter = request.GET.get("warranty")
    seller_filter = request.GET.get("seller")

    if price_filter:
        products = products.filter(price__lte=price_filter)
    if category_filter:
        products = products.filter(category__name=category_filter)
    if brand_filter:
        products = products.filter(brand__name=brand_filter)
    if warranty_filter:
        products = products.filter(warranty__name=warranty_filter)
    if seller_filter:
        products = products.filter(seller__name=seller_filter)

    return render(
        request,
        "products_page.html",
        {
            "banner_image": banner_image,
            "products": products,
            "highest_price": highest_price,
            "categories": categories,
            "brands": brands,
            "warranties": warranties,
            "sellers": sellers,
        },
    )
