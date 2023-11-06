import pytest
from rest_framework.test import APIClient
from main.models import User, Shop, Product, ProductInfo


@pytest.fixture()
def client():
    return APIClient()


@pytest.fixture()
def user():
    return User.objects.create_user(first_name='first_name', last_name='last_name', email='netology@bk.ru',
                             password='april082004', company='company', position='position')


@pytest.fixture()
def shop():
    return Shop.objects.create(name='name', url='url')


@pytest.fixture()
def product(shop):
    product = Product.objects.create(name='product')
    external_id = 10
    quantity = 10
    price = 10
    price_rrc = 15
    return ProductInfo.objects.create(product=product, external_id=external_id, quantity=quantity,
                               shop=shop, price=price, price_rrc=price_rrc)


@pytest.mark.django_db
def test_post_user(client):
    data = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'email': 'netology@bk.ru',
        'password': 'april082004',
        'company': 'company',
        'position': 'position'
    }
    response_post = client.post('http://127.0.0.1:8000/api/v1/user/register', data=data)
    assert response_post.status_code == 201


@pytest.mark.django_db
def test_get_user(client, user):
    response_get = client.get('http://127.0.0.1:8000/api/v1/users/')
    assert response_get.status_code == 200
    data = response_get.json()
    assert len(data) == 1

    response_get_retrieve = client.get(f'http://127.0.0.1:8000/api/v1/user/{user.id}')
    assert response_get_retrieve.status_code == 200

    data = response_get_retrieve.json()
    assert data['email'] == 'netology@bk.ru'


@pytest.mark.django_db
def test_get_shop(client, shop):
    response_get = client.get('http://127.0.0.1:8000/api/v1/shops/')
    assert response_get.status_code == 200

    data = response_get.json()
    assert len(data) == 1

    response_get_retrieve = client.get(f'http://127.0.0.1:8000/api/v1/shop/{shop.id}')
    assert response_get_retrieve.status_code == 200

    data_ = response_get_retrieve.json()
    assert data_['id'] == shop.id


@pytest.mark.django_db
def test_get_product(client, product):
    response_get = client.get(f'http://127.0.0.1:8000/api/v1/product?title={product.product}')
    assert len(ProductInfo.objects.all()) == 1

    assert response_get.status_code == 200
    data = response_get.json()
    assert product.product.name == data[0]['product']


# @pytest.mark.django_db
# def test_post_contact(client, user):
#     user.is_authenticated
#     data_ = {
#         'user': user,
#         'city': 'city',
#         'street': 'street',
#         'phone': 'phone'
#     }
#     response_post = client.post('http://127.0.0.1:8000/api/v1/contact', data=data_)
#
#     assert response_post.status_code == 201




