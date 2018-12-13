from django.db import models
from products.models import Product


class Status(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)

    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return 'Статус {}'.format(self.name)

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class Order(models.Model):

    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)  # !!!!!!!!!!
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_adress = models.CharField(max_length=160, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)  # Несколько строк
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return 'Заказ {} от {} создан:{}, статус:{}'.format(self.id, self.customer_name,
                                                            self.created, self.status.name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductInOrder(models.Model):
    price_pre_item = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)  # price * number

    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)
    number = models.IntegerField(default=1)
    is_active = models.ForeignKey(Status, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Продукт в корзине: {}'.format(self.product.id,)  # В каком виде возвращает данные модели

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
