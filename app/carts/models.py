from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models, transaction
from django.db.models import CASCADE, F
from goods.models import Goods

User = get_user_model()


class Cart(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    quantity_of_goods = models.IntegerField('총 상품 수량', default=0, null=True)

    @property
    def total_pay(self):
        payment = 0
        for ins in self.item.all():
            if ins.discount_payment() is not None:
                payment += ins.discount_payment()
            else:
                payment += ins.sub_total()
        return payment


class CartItem(models.Model):
    quantity = models.IntegerField(default=1,
                                   validators=[MinValueValidator(1), MaxValueValidator(50)])
    cart = models.ForeignKey(Cart, on_delete=CASCADE, related_name='item', null=True)
    goods = models.ForeignKey(Goods, on_delete=CASCADE, related_name='item', )
    order = models.ForeignKey('order.Order',
                              on_delete=models.SET_NULL,
                              null=True,
                              related_name='item',
                              )

    def sub_total(self):
        return self.goods.price * self.quantity

    def discount_payment(self):
        try:
            if type(self.goods.sales.discount_rate) is int:
                return ((100 - self.goods.sales.discount_rate) * 0.01) * (self.goods.price * self.quantity)
            return self.sub_total()
        except AttributeError:
            return self.sub_total()

    @transaction.atomic
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.cart.quantity_of_goods = F('quantity_of_goods') + 1
        self.cart.save()

    @transaction.atomic
    def delete(self, using=None, keep_parents=False):
        super().save()
        self.cart.quantity_of_goods = F('quantity_of_goods') - 1
        self.cart.save()
