from django.db import models
from django.shortcuts import render


class Product(models.Model):
    def product_list(request):
        products = Product.objects.all()  # Получаем все продукты (пряники)
        return render(request, 'admin_panel/product_list.html', {'products': products})

    image = models.ImageField(blank=True, upload_to='products/')
    name=models.CharField(  
        verbose_name=('Название пряника'),
        max_length=50, 
    )  
  
    description=models.CharField(  
        verbose_name=('Состав пряника'),  
        max_length=100, 
    )  
  
    price=models.IntegerField(  
        verbose_name="Цена пряника"  
    )  

    class Meta:  
        verbose_name="Пряник"  
        verbose_name_plural="Пряники"  
  
    def __str__(self):  
        return self.name
