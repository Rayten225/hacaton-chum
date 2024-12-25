from django.contrib import admin
from orders.models import Order
from django.contrib.admin import ModelAdmin

@admin.register(Order)
class ProductAdmin(ModelAdmin):
    list_display = ('FIO','number', 'deadline', 'organization','price','address','email')
    fieldsets = (
        ('Client info', dict(
            fields=('FIO', 'number', 'formatted_order_items', 'deadline', 'organization', 'price', 'address', 'email'))),
    )
    readonly_fields = ('FIO','number', 'formatted_order_items', 'organization','price','address','email')