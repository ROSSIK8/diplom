from django.contrib import admin
from .models import User, Shop, Product, ProductInfo, ShopCategory, Contact


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'owner', 'categories']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'shop', 'quantity', 'price', 'price_rrc']


@admin.register(ShopCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'shop', 'category']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'city', 'street', 'phone']


