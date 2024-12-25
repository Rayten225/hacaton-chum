from django.shortcuts import render
from django.template.context_processors import request

from shop.models import Product


def admin_main(request):
    products = Product.objects.all()  # Получаем все продукты (пряники)
    return render(request, 'admin_panel/admin_main.html', {'user': request.user, 'products': products})