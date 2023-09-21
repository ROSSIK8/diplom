from django.urls import path
from .views import *


urlpatterns = [
    path('users/', UsersView.as_view()),
    path('user/<int:pk>', UserDetailView.as_view()),
    path('user/register', RegisterView.as_view(), name='user-register'),
    path('shops/', ShopsView.as_view()),
    path('shop/<int:pk>', ShopDetailView.as_view()),
    path('categories', CategoryView.as_view(), name='categories'),
    path('products', ProductView.as_view(), name='products'),
    path('product', ProductInfoView.as_view(), name='product_info'),
    path('contact', ContactView.as_view(), name='contact'),
]
