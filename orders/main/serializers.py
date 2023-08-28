from rest_framework import serializers
from .models import User, Shop, Product, ProductInfo, Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['city', 'street', 'house', 'apartment', 'phone']


class UserSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(read_only=True, many=True)
    shops = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'type_user', 'email', 'contacts', 'shops']


class ShopSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()

    class Meta:
        model = Shop
        fields = ['id', 'name', 'owner', 'url']


class ProductInfoSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()

    class Meta:
        model = ProductInfo
        fields = ['product', 'quantity', 'price', 'price_rrc']


class ShopDetailSerializer(serializers.ModelSerializer):
    product_infos = ProductInfoSerializer(many=True, read_only=True)
    owner = serializers.StringRelatedField()

    class Meta:
        model = Shop
        fields = ['id', 'name', 'owner', 'product_infos']


# class ProductSerializer(serializers.ModelSerializer):
#     product_infos = ProductInfoSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Product
#         fields = ['id', 'name', 'product_infos']



