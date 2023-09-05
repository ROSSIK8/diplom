from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.core.mail import send_mail
import random


class RegisterView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            code = random.randint(111111, 999999)
            send_mail('Код подтверждения', f'{code}', settings.EMAIL_HOST_USER, [request.data['email']])
            confirmation_code = input('Введите код подтверждения из письма: ')
            if confirmation_code == str(code):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            while confirmation_code != str(code):
                confirmation_code = input('Введённый код не верный, повторите попытку: ')
                if confirmation_code == str(code):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class UsersView(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class ShopsView(ListCreateAPIView):
#     queryset = Shop.objects.all()
#     serializer_class = ShopSerializer
#
#
# class ShopDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Shop.objects.all()
#     serializer_class = ShopDetailSerializer






