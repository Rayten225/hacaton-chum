from django.contrib import admin
from orders.models import Order
from django.contrib.admin import ModelAdmin

@admin.register(Order)
class ProductAdmin(ModelAdmin):
    list_display = ('FIO','number', 'order', 'deadline', 'organization','price','address','email')
    fieldsets = (
        ('Client info', {'fields': ('FIO','number', 'order', 'deadline', 'organization','price','address','email')}),
    )
    readonly_fields = ('FIO','number', 'order', 'organization','price','address','email')