from django.db import models

class Order(models.Model):  
    FIO=models.CharField(  
        verbose_name=('ФИ клиента'),  
        max_length=50, 
    )  
  
    number=models.IntegerField(  
        verbose_name=('Номер клиента'),  
    )  
  
    order=models.TextField(  
        verbose_name="Заказ клиента",
        max_length=9999, 
    )

    price=models.IntegerField(  
        verbose_name="Итоговая сумма"  
    )

    class Meta:  
        verbose_name="Заказ"  
        verbose_name_plural="Заказы"  
  
    def __str__(self):  
        return self.FIO

