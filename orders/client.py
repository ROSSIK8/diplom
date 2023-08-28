import requests


response = requests.patch('http://127.0.0.1:8000/api/v1/shop/2',
                          json={
                                "id": 2,
                                "name": "Игрушки",
                                "owner": "Продавец_1",
                                "product_infos": [
                                    {
                                        "product": "Юла",
                                        "quantity": 3,
                                        "price": 4,
                                        "price_rrc": 7
                                    },
                                    {
                                        "product": "Машинка",
                                        "quantity": 50,
                                        "price": 30,
                                        "price_rrc": 60
                                    }
                                ]
                            })


# response = requests.get('http://127.0.0.1:8000/api/v1/shop/5')

print(response.json())
