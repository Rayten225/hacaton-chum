from shop.models import Product
from rest_framework import serializers

class ProductCreationSerializer(serializers.ModelSerializer): #Создаем класс
    class Meta: #Класс мета нужен лоя вывода полей в апи
        model = Product #Указываем с каким обьектом работаем 
        fields = ['name', 'description', 'price'] #Указываем какие поля будут выводится в апи
        extra_kwargs = {  #Сообщения с ошибками 
            "name": {  
                "error_messages": {"required": "Невалидное имя.", "blank": "Пожалуйста, заполните поле имени."}},  
            "description": {  
                "error_messages": {"required": "Невалидное описание.", "blank": "Пожалуйста, заполните поле описания."}},  
            "price": {  
                "error_messages": {"required": "Невалидная цена.", "blank": "Пожалуйста, заполните поле цены."}},  
        }  
