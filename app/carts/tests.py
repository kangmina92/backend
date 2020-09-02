import os
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from carts.models import CartItem
from config import settings
from config.settings.base import ROOT_DIR
from goods.models import Goods

User = get_user_model()


class Cart_test(APITestCase):

    def setUp(self) -> None:
        self.user = User(username='User_test', password='1111', email='cccc@c.com')
        self.user.set_password(self.user.password)
        self.user.save()

        image = settings.base.MEDIA_ROOT + '/mssql.jpeg'

        for i in range(5):
            test_file = SimpleUploadedFile(name='test_image.jpeg', content=open(image, 'rb', ).read(),
                                           content_type="image/jpeg"
                                           )
            test_file2 = SimpleUploadedFile(name='test_image.jpeg', content=open(image, 'rb', ).read(),
                                            content_type="image/jpeg"
                                            )

            self.goods = Goods.objects.create(img=test_file, info_img=test_file2, title='상품명',
                                              short_desc='간단설명', price='555')


    def test_cart_item_create(self):
        user = self.user
        self.client.force_authenticate(user=user)

        data = {
            "goods": 1,
            "quentity": 3,
            "cart": 1
        }

        response = self.client.post(f'/api/cart/{user.pk}/item', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data['goods'], response.data['goods'])
        self.assertEqual(data['cart'], response.data['cart'])

    def test_cart_item_list(self):
        user = self.user
        self.client.force_authenticate(user=user)
        test_goods = Goods.objects.all()

        for i in test_goods:
            self.carts = CartItem.objects.create(cart=user.cart, goods=i, quantity=4)

        cart_item_list = CartItem.objects.values()

        response = self.client.get(f'/api/cart/{user.pk}/item')

        for query_ins, response_ins in zip(cart_item_list, response.data):
            self.assertEqual(query_ins['goods_id'], response_ins['goods']['id'])
            self.assertEqual(query_ins['id'], response_ins['id'])


    def test_cart_item_update(self):
        user = self.user
        self.client.force_authenticate(user=user)
        # test_goods = Goods.objects.first()

        data = {
            "goods": 1,
            "quentity": 3,
            "cart": 1
        }

        response = self.client.post(f'/api/cart/{user.pk}/item', data=data)
        print('first', response)

        # data = {
        #     "goods": test_goods.pk,
        #     "quentity": 2,
        #     "cart": user.cart
        # }
        #
        #
        # item = CartItem.objects.first()
        #
        # response = self.client.patch(f'/api/cart/{user.pk}/item/{test_goods.id}', data=data)


        self.fail()
