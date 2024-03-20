from django.contrib import admin

from orders.models import OrderModel, OrderItemModel

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItemModel

@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_price', 'created_at']
    inlines = [OrderItemInline]

admin.site.register(OrderItemModel)