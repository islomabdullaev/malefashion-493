from django.contrib import admin

from orders.models import OrderModel, OrderItem

# Register your models here.

admin.site.register(OrderModel)
admin.site.register(OrderItem)