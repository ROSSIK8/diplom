from rest_framework import serializers
from .models import User, Shop, Product, ProductInfo, Contact, Category


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['city', 'street', 'house', 'apartment', 'phone']


class UserSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(read_only=True, many=True)
    password = serializers.CharField(min_length=8, max_length=65, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'type', 'company', 'position', 'contacts', 'password']
        read_only_fields = ['id']


class ShopSerializer(serializers.ModelSerializer):
    # owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    owner = serializers.StringRelatedField()

    def validate(self, data):
        data['owner'] = self.context['request'].user
        return data

    def create(self, validated_data):
        return Shop.objects.create(**validated_data)

    class Meta:
        model = Shop
        fields = ['id', 'name', 'owner', 'url']


class CategorySerializer(serializers.ModelSerializer):
    shops = serializers.StringRelatedField(many=True)

    class Meta:
        model = Category
        fields = ['name', 'shops']


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


class ProductSerializer(serializers.ModelSerializer):
    product_infos = ProductInfoSerializer(many=True, read_only=True)
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'product_infos']


