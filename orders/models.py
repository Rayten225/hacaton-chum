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
        verbose_name=("Заказ клиента"),
        max_length=9999, 
    )

    deadline=models.CharField(  
        verbose_name=("Дата доставки"),
        max_length=10,
    )
    organization=models.CharField(  
        verbose_name=("Название организации"), 
        max_length=100,
    )
    
    price=models.IntegerField(  
        verbose_name=("Итоговая сумма"),
    )

    address=models.CharField(  
        verbose_name=("Адрес доставки"),
        max_length=100,
    )

    email=models.CharField(  
        verbose_name=("Почта клиента"),
        max_length=100,
    )

    class Meta:  
        verbose_name="Заказ"  
        verbose_name_plural="Заказы"  
  
    def __str__(self):  
        return self.FIO

