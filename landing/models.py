from django.db import models


class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=256)  # !!!!!!!!!!

    def __str__(self):
        return 'Пользователь {} name:{}'.format(self.email, self.name)  # В каком виде возвращает данные модели

    class Meta:
        verbose_name = 'Мой Саб'
        verbose_name_plural = 'Моя армия сабов'
