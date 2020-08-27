import os

from django.contrib.auth import get_user_model
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

    def test_cart_create(self):
        user = self.user

        goods = Goods.objects.first()

        data = {
            "goods": goods.pk,
            "quantity": 3,
            "user": user.pk
        }

        response = self.client.post(f'/api/carts', data=data)


        self.fail()
