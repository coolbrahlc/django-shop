from django.contrib import admin
from  .models import *


class SubscriberAdmin(admin.ModelAdmin):

    # list_display = ['name', 'email']         # Какие поля выводить в админке
    list_display = [field.name for field in Subscriber._meta.fields]

    fields = ['email']                          # Что отображать при нажатии на строку
    # exclude = ['email']                       # Что спрятать

    list_filter = ['name', 'email']                      # По каким полям применть фильтр
    search_fields = ['name', 'email']                    # Применять поиск по заданным полям

    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)