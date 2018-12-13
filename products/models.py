from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)  # !!!!!!!!!!
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(blank=True, null=True, default=None)  # Несколько строк
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Товар {}  цена:{}'.format(self.price, self.name)  # В каком виде возвращает данные модели

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='fold')
    is_active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Изображение {} создано:{}'.format(self.product, self.created)  # В каком виде возвращает данные модели

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'