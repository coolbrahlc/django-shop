from django.db import models
from django.db.models.signals import post_save
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

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    price_pre_item = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)  # price * number

    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)
    number = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    # is_active = models.ForeignKey(Status, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Продукт в корзине: {}'.format(self.product.id,)  # В каком виде возвращает данные модели

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):                    # !!!!!!!!!!
        price_per_item_temp = self.product.price        # Указываем на цену товара из Product
        self.price_pre_item = price_per_item_temp
        self.total_price = self.number * price_per_item_temp
        '''
        tmp_order = self.order
        all_products_in_oder = ProductInOrder.objects.filter(order=tmp_order, is_active=True)   # !!!!!!!!!!

        order_total_price = 0

        for item in all_products_in_oder:
            order_total_price += item.total_price
        self.order.total_amount = order_total_price

        self.order.save(force_update=True)
        '''
        super(ProductInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):

    tmp_order = instance.order          # instance вмсето self
    all_products_in_oder = ProductInOrder.objects.filter(order=tmp_order, is_active=True)  # !!!!!!!!!!

    order_total_price = 0

    for item in all_products_in_oder:
        order_total_price += item.total_price

    instance.order.total_amount = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)