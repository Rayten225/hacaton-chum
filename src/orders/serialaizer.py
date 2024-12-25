from orders.models import Order
from rest_framework import serializers
from orders.validations import custom_validate_order
class OrdersCreationSerializer(serializers.ModelSerializer): #Создаем класс
    class Meta: #Класс мета нужен лоя вывода полей в апи
        model = Order #Указываем с каким обьектом работаем 
        fields = ['FIO','number', 'order', 'deadline', 'organization','price','address','email'] #Указываем какие поля будут выводится в апи
        extra_kwargs = {  #Сообщения с ошибками
            "FIO": {
                "error_messages": {"required": "Невалидное ФИ.", "blank": "Пожалуйста, заполните поле ФИ."}},
            "number": {
                "error_messages": {"required": "Невалидный номер.", "blank": "Пожалуйста, заполните поле номера."}},
            "order": {
                "error_messages": {"required": "Невалидный заказ.", "blank": "Пожалуйста, заполните поле заказа."}},
            "deadline": {
                "error_messages": {"required": "Невалидная дата доставки.", "blank": "Пожалуйста, заполните поле даты доставки."}},
            "organization": {
                "error_messages": {"required": "Невалидная организация.", "blank": "Пожалуйста, заполните поле оргпнизации."}},
            "price": {
                "error_messages": {"required": "Невалидная цена.", "blank": "Пожалуйста, заполните поле цены."}},
            "address": {
                "error_messages": {"required": "Невалидный адрес.", "blank": "Пожалуйста, заполните поле адреса."}},
            "email": {
                "error_messages": {"required": "Невалидный email.", "blank": "Пожалуйста, заполните поле email."}},
        }
    def create(self, validated_data):
        order = Order.objects.create_order(
            FIO=validated_data['FIO'],
            number=validated_data['number'],
            order=validated_data.get('order'),
            deadline=validated_data.get('deadline'),
            organization=validated_data.get('organization'),
            price=validated_data.get('price'),
            address=validated_data.get('address'),
            email=validated_data.get('email'),
        )
        return order

    # def validate(self, data):
    #     custom_validate_order(data)
    #     return data