from rest_framework import serializers
from .models import User, Shop, Product, ProductInfo, Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['city', 'street', 'house', 'apartment', 'phone']


class UserSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(read_only=True, many=True)
    password = serializers.CharField(min_length=8, max_length=65, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'company', 'position', 'contacts', 'password']
        read_only_fields = ['id']

    def validate(self, attrs):
        email = attrs.get('email', '')
        required_items = {
            'first_name': ['first_name required'],
            'last_name': ['last_name required'],
            'email': ['email required'],
            'password': ['password required'],
            'company': ['company required'],
            'position': ['position required']
        }

        errors = {}
        for key, val in required_items.items():
            if key not in attrs:
                errors[key] = val

        if errors:
            raise serializers.ValidationError(errors)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({
                'detail': 'Email is already in use'
            })
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



# class ShopSerializer(serializers.ModelSerializer):
#     owner = serializers.StringRelatedField(default=serializers.CurrentUserDefault())

    # def create(self, validated_data):
    #     shop = Shop.objects.create(
    #         name=validated_data['name'],
    #         owner=validated_data['owner'],
    #         url=validated_data['url'],
    #     )
    #
    #     return shop

#     class Meta:
#         model = Shop
#         fields = ['id', 'name', 'owner', 'url']
#
#
# class ProductInfoSerializer(serializers.ModelSerializer):
#     product = serializers.StringRelatedField()
#
#     class Meta:
#         model = ProductInfo
#         fields = ['product', 'quantity', 'price', 'price_rrc']
#
#
# class ShopDetailSerializer(serializers.ModelSerializer):
#     product_infos = ProductInfoSerializer(many=True, read_only=True)
#     owner = serializers.StringRelatedField()
#
#     class Meta:
#         model = Shop
#         fields = ['id', 'name', 'owner', 'product_infos']


# class ProductSerializer(serializers.ModelSerializer):
#     product_infos = ProductInfoSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Product
#         fields = ['id', 'name', 'product_infos']



