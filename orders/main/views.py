from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, ListAPIView
from .serializers import UserSerializer, ShopSerializer, ShopDetailSerializer
from rest_framework.response import Response
from .models import User, Shop, Product


class UsersView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ShopsView(ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def post(self, request):
        review = ShopSerializer(data=request.data)
        if review.is_valid():
            review.save()

        return Response({'status': 'OK'})


class ShopDetailView(RetrieveAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopDetailSerializer

    def patch(self, request, pk):
        shop = Shop.objects.get(pk=pk)
        serializer = ShopDetailSerializer(shop, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)





