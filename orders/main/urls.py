from django.urls import path, include
from .views import *


urlpatterns = [
    path('users/', UsersView.as_view()),
    path('user/<int:pk>', UserDetailView.as_view()),
    path('user/register', RegisterView.as_view(), name='user-register'),
    path('user/login', LoginAccount.as_view(), name='user-login'),
    path('user/logout', LogoutAccount.as_view(), name='user-logout'),
    # path('user/auth/', include('rest_framework.urls'), name='user-login'),
    path('email/confirmation', EmailConfirmationView.as_view(), name='email-confirmation'),
    path('shops/', ShopsView.as_view()),
    path('shop/<int:pk>', ShopDetailView.as_view()),
    path('categories', CategoryView.as_view(), name='categories'),
    path('product', ProductInfoView.as_view(), name='product-info'),
    path('contact', ContactView.as_view(), name='contact'),
    path('basket', BasketView.as_view(), name='basket'),
    path('order', OrderView.as_view(), name='order'),
]
