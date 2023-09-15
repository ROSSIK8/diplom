from django.urls import path
# from .views import UsersView, UserDetailView, ShopsView, ShopDetailView
from .views import *

urlpatterns = [
    path('users/', UsersView.as_view()),
    path('user/<int:pk>', UserDetailView.as_view()),
    path('shops/', ShopsView.as_view()),
    path('shop/<int:pk>', ShopDetailView.as_view()),
    path('user/register', RegisterView.as_view(), name='user-register'),
    path('categories', CategoryView.as_view(), name='categories'),
]
