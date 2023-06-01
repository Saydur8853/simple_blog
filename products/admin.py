from django.contrib import admin

# Register your models here.
from .models import Category, Brand, Warranty, Seller, Product, BannerImage

admin.site.register(BannerImage)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Warranty)
admin.site.register(Seller)
admin.site.register(Product)
