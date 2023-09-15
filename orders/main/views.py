from django.contrib.auth.password_validation import validate_password
from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .models import User, Shop, Category, Product, ProductInfo
from .permissions import IsOwnerOrReadOnly, IsSalesmanOrReadOnly
from .serializers import UserSerializer, ShopSerializer, ShopDetailSerializer, CategorySerializer, ProductSerializer, \
    ProductInfoSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.core.mail import send_mail
import random


class RegisterView(APIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        if {'first_name', 'last_name', 'email', 'password', 'company', 'position'}.issubset(request.data):
            try:
                validate_password(request.data['password'])
                user_serializer = UserSerializer(data=request.data)
                if user_serializer.is_valid():
                    code = random.randint(111111, 999999)
                    send_mail('Код подтверждения', f'{code}', settings.EMAIL_HOST_USER, [request.data['email']])
                    confirmation_code = input('Введите код подтверждения из письма: ')
                    if confirmation_code == str(code):
                        user_serializer.save()
                        return Response(user_serializer.data, status=status.HTTP_201_CREATED)
                    for _ in range(2):
                        confirmation_code = input('Введённый код не верный, повторите попытку: ')
                        if confirmation_code == str(code):
                            user_serializer.save()
                            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
                    print('Попытки закончились')
                    return Response(user_serializer.data, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return JsonResponse({'Status': False, 'Errors': user_serializer.errors})
            except Exception as password_error:
                error_array = []
                # noinspection PyTypeChecker
                for item in password_error:
                    error_array.append(item)
                return JsonResponse({'Status': False, 'Errors': {'password': error_array}})
        return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})


class UsersView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class ShopsView(ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [IsSalesmanOrReadOnly]


class ShopDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductInfoView(ListAPIView):
    queryset = ProductInfo.objects.all()
    serializer_class = ProductInfoSerializer





