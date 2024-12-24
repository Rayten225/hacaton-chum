from django.db import models

class Product(models.Model):  
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
