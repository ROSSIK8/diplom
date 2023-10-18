from rest_framework import serializers
from .models import User, Shop, Product, ProductInfo, Contact, Category, Basket, Order, EmailConfirmation


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id', 'user', 'city', 'street', 'phone']
        read_only_fields = ['id']
        extra_kwargs = {
            'user': {'write_only': True}
        }


class OrderSerializer(serializers.ModelSerializer):
    shop = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = ['id', 'shop', 'product', 'quantity']


class BasketSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Basket
        fields = ['id', 'orders']


class UserSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(read_only=True, many=True)
    password = serializers.CharField(min_length=8, max_length=65, write_only=True)

    # def create(self, validated_data):
    #     print(validated_data)
    #
    #     return User.objects.create(**validated_data)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'type', 'company', 'position', 'contacts', 'password']
        read_only_fields = ['id', 'type']


class EmailConfirmationSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmailConfirmation
        fields = ['code']


class ShopSerializer(serializers.ModelSerializer):
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
    shops = ShopSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'shops']


class ProductInfoSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    shop = serializers.StringRelatedField()

    class Meta:
        model = ProductInfo
        fields = ['product', 'shop', 'quantity', 'price', 'price_rrc']


class ProductInfoForShopSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()

    class Meta:
        model = ProductInfo
        fields = ['product', 'quantity', 'price', 'price_rrc']


class ShopDetailSerializer(serializers.ModelSerializer):
    product_infos = ProductInfoForShopSerializer(many=True, read_only=True)
    owner = serializers.StringRelatedField()

    class Meta:
        model = Shop
        fields = ['id', 'name', 'owner', 'product_infos', 'url']
        extra_kwargs = {
            'url': {'write_only': True}
        }


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'category']










