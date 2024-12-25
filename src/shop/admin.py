from django.contrib import admin
from shop.models import Product
from django.contrib.admin import ModelAdmin



@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('name','description', 'price')
    search_fields = ('name', 'description')
    list_filter = ('price',)
    fieldsets = (
        ('Product info', {'fields': ('name', 'description', 'price', 'image')}),
    )