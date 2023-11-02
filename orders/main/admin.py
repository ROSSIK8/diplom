from django.contrib import admin
from .models import User, Shop, Product, ProductInfo, ShopCategory, Contact, Basket, Order, EmailConfirmation


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user', 'categories']


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


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'shop', 'product', 'quantity']


@admin.register(EmailConfirmation)
class EmailConfirmationAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'code', 'state']

