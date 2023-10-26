from django.contrib.auth.password_validation import validate_password
from django.http import JsonResponse, Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from django.conf import settings
from django.core.mail import send_mail

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from .models import User, Shop, Category, Product, ProductInfo, Contact, Basket, Order, EmailConfirmation
from .permissions import IsOwnerOrReadOnly, IsSalesmanOrReadOnly
from .serializers import UserSerializer, ShopSerializer, ShopDetailSerializer, CategorySerializer, ProductSerializer, \
    ProductInfoSerializer, ContactSerializer, BasketSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework import status
import random


class RegisterView(APIView):

    "View для регистрации пользователя"

    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        if {'first_name', 'last_name', 'email', 'password', 'company', 'position'}.issubset(request.data):
            try:
                validate_password(request.data['password'])
                user_serializer = UserSerializer(data=request.data)
                if user_serializer.is_valid():
                    user_serializer.save()
                    if user_serializer.data['type'] == 'buyer':
                        user_id = user_serializer.data['id']
                        Basket.objects.create(user_id=user_id)
                        return Response(user_serializer.data, status=status.HTTP_201_CREATED)
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


class EmailConfirmationView(APIView):

    "View для подтверждения email"

    def get(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'Status': False, 'Error': 'Требуется войти'}, status=403)
        code = random.randint(111111, 999999)
        send_mail('Код подтверждения', f'{code}', settings.EMAIL_HOST_USER, [request.user.email])
        EmailConfirmation.objects.create(user_id=request.user.id, email=request.user.email, code=code)

        return Response({'text': 'Введите код для подтверждения'})

    def post(self, request):
        email_code = EmailConfirmation.objects.filter(user=request.user)[0]
        if {'code'}.issubset(request.data):
            request_code = request.data['code']
            if request_code == email_code.code:
                email_code.state = 'Confirmed'
                email_code.save()
                return JsonResponse({'Status': 'Подтвержден'})
            return JsonResponse({'Status': 'Неподтвержден'})
        return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})


class LoginAccount(APIView):

    "View для входа"

    def post(self, request, *args, **kwargs):

        if {'email', 'password'}.issubset(request.data):
            user = User.objects.filter(email=request.data['email'], password=request.data['password'])[0]

            if user is not None:
                if user.is_active:
                    token = Token.objects.get_or_create(user=user)

                    return JsonResponse({'Status': True, 'Token': token[0].key})

            return JsonResponse({'Status': False, 'Errors': 'Не удалось авторизовать'})

        return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})


class LogoutAccount(APIView):

    "View для выхода"

    def delete(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'Status': False, 'Error': 'Требуется войти'}, status=403)
        Token.objects.get(user=request.user).delete()
        return JsonResponse({'Status': True})


class UsersView(ListAPIView):

    "View для просмотра пользователей"

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserDetailView(RetrieveUpdateDestroyAPIView):

    "View для просмотра пользователя"

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class ShopsView(ListCreateAPIView):

    "View для просмотра магазинов"

    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [IsSalesmanOrReadOnly]


class ShopDetailView(RetrieveUpdateDestroyAPIView):

    "View для просмотра магазина"

    queryset = Shop.objects.all()
    serializer_class = ShopDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]


class CategoryView(ListAPIView):

    "View для просмотра категорий"

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductInfoView(ListAPIView):

    "View для поиска товаров"

    serializer_class = ProductInfoSerializer

    def get_queryset(self):
        queryset = ProductInfo.objects.all()
        try:
            product = Product.objects.get(name=self.request.query_params.get('title'))
            queryset = queryset.filter(product=product)
            return queryset
        except ObjectDoesNotExist:
            raise Http404


class ContactView(APIView):

    "View для работы с контактами"

    def get(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'Status': False, 'Error': 'Требуется войти'}, status=403)

        contact = Contact.objects.filter(user_id=request.user.id)
        serializer = ContactSerializer(contact, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'Status': False, 'Error': 'Требуется войти'}, status=403)

        if {'city', 'street', 'phone'}.issubset(request.data):
            request.data['user'] = request.user.id
            contact_serializer = ContactSerializer(data=request.data)

            if contact_serializer.is_valid():
                contact_serializer.save()
                return JsonResponse({'Status': True})
            else:
                return JsonResponse({'Status': False, 'Errors': contact_serializer.errors})

        return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})

    def put(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'Status': False, 'Error': 'Требуется войти'}, status=403)

        if 'id' in request.data:
            contact = Contact.objects.filter(id=request.data['id'], user_id=request.user.id).first()
            if contact:
                serializer = ContactSerializer(contact, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({'Status': True})
                else:
                    return JsonResponse({'Status': False, 'Errors': serializer.errors})

        return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})

    def delete(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'Status': False, 'Error': 'Требуется войти'}, status=403)

        Contact.objects.filter(user=request.user).delete()
        return JsonResponse({'Status': 'deleted'})


class BasketView(APIView):

    "View для просмотра корзины"

    def get(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'Status': False, 'Error': 'Требуется войти'}, status=403)

        basket = Basket.objects.filter(user_id=request.user.id)
        basket_serializer = BasketSerializer(basket, many=True)
        return Response(basket_serializer.data)


class OrderView(APIView):

    "View для работы с заказами"

    def post(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'Status': False, 'Error': 'Требуется войти'}, status=403)
        try:
            shop = Shop.objects.filter(name=request.data['shop'])[0]
            product = shop.product_infos.filter(product__name=request.data['product'])[0].product
            quantity = int(request.data['quantity'])
            order = Order.objects.create(user=request.user, shop=shop, product=product, quantity=quantity)
            Basket.objects.filter(user=request.user).all()[0].orders.add(order)
            return JsonResponse({'Status': True})
        except IndexError:
            return JsonResponse({'Status': False, 'Error': 'Неверный запрос'}, status=400)

    def put(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'Status': False, 'Error': 'Требуется войти'}, status=403)

        if 'id' in request.data:
            order = Order.objects.filter(id=request.data['id'], user_id=request.user.id).first()
            if order:
                order_serializer = OrderSerializer(order, data=request.data)
                if order_serializer.is_valid():
                    order_serializer.save()
                    return JsonResponse({'Status': True})
                else:
                    return JsonResponse({'Status': False, 'Errors': order_serializer.errors})

        return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})

    def delete(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'Status': False, 'Error': 'Требуется войти'}, status=403)

        if 'id' in request.data:
            order = Order.objects.filter(id=request.data['id']).first()
            if order.user == request.user:
                order.delete()
                return JsonResponse({'Status': True})
            return JsonResponse({'Status': False, 'Errors': 'Ошибка разрешения'})
        return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})
