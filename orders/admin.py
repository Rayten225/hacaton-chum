from django.contrib import admin
from orders.models import Order
from django.contrib.admin import ModelAdmin

@admin.register(Order)
class ProductAdmin(ModelAdmin):
    list_display = ('FIO','number', 'order', 'price')
    fieldsets = (
        ('Client info', {'fields': ('FIO','number', 'order', 'price')}),
    )
    readonly_fields = ('FIO', 'number', 'order', 'price',)