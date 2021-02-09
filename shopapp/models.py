from django.db import models
from django.contrib.auth.models import User
from parser_site.models import *

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=100, null=True)

    class Meta:
        verbose_name='Покупатель'
        verbose_name_plural='Покупатели'

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    class Meta:
        verbose_name='Заказ'
        verbose_name_plural='Заказы'

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(CardProduct, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(verbose_name='Количество', blank=True, null=True, default=0)
    date_added = models.DateField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return  total

    class Meta:
        verbose_name='Позиция заказа'
        verbose_name_plural='Позиции заказа'


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    adress = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    zip = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='Адрес доставки'
        verbose_name_plural='Адреса доставки'


    def __str__(self):
        return self.adress



