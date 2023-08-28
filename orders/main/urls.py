from django.urls import path
from .views import UsersView, UserDetailView, ShopsView, ShopDetailView

urlpatterns = [
    path('users/', UsersView.as_view()),
    path('user/<int:pk>', UserDetailView.as_view()),
    path('shops/', ShopsView.as_view()),
    path('shop/<int:pk>', ShopDetailView.as_view()),
]