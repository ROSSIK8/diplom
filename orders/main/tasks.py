from __future__ import absolute_import

import time

from django.contrib.auth.password_validation import validate_password
from django.http import JsonResponse
from orders.celery import app
from rest_framework import status
from rest_framework.response import Response

from .models import Basket
from .serializers import UserSerializer


@app.task
def register_user(self, request):
        start = time.time()
        if {'first_name', 'last_name', 'email', 'password', 'company', 'position'}.issubset(request.data):
            try:
                validate_password(request.data['password'])
                user_serializer = UserSerializer(data=request.data)
                if user_serializer.is_valid():
                    user_serializer.save()
                    if user_serializer.data['type'] == 'buyer':
                        user_id = user_serializer.data['id']
                        Basket.objects.create(user_id=user_id)
                        print(time.time() - start)
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