import json
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.utils.html import format_html


class OrderManager(BaseUserManager):
    use_in_migrations = True

    def create_order(self, email, **extra_fields):
        if not email:
            raise ValueError('The email must be set')

        order = self.model(email=email, **extra_fields)
        order.save()
        return order


class Order(models.Model):
    order = models.CharField(max_length=5000, verbose_name="Данные заказа (JSON)")

    def formatted_order_items(self):
        """
        Парсит JSON из order и выводит товары построчно в формате HTML.
        """
        try:
            # Проверка на пустое поле
            if not self.order:
                return "Поле данных заказа пустое"

            # Выводим содержимое order для отладки
            print("Содержимое order:", self.order)

            # Парсим JSON
            data = json.loads(self.order)
            print("Parsed data:", data)

            # Теперь data уже список, и нет необходимости искать 'order'
            if not isinstance(data, list):
                return "Поле 'order' должно содержать список товаров"

            # Форматируем товары в HTML-строку
            items_html = "".join(
                [f"<li>{item['product']} — {item['quantity']} шт. ({item['price']}₽)</li>" for item in data])
            return format_html(f"<ul>{items_html}</ul>")
        except json.JSONDecodeError as e:
            return f"Некорректный JSON: {e}"
        except Exception as e:
            return f"Ошибка: {e}"

    formatted_order_items.short_description = "Товары в заказе"

    FIO = models.CharField(
        verbose_name="ФИ клиента",
        max_length=50,
    )
    number = models.CharField(
        verbose_name="Номер клиента",
        max_length=100,
    )
    deadline = models.CharField(
        verbose_name="Дата доставки",
        max_length=10,
    )
    organization = models.CharField(
        verbose_name="Название организации",
        max_length=100,
    )
    price = models.CharField(
        verbose_name="Итоговая сумма",
        max_length=100,
    )
    address = models.CharField(
        verbose_name="Адрес доставки",
        max_length=100,
    )
    email = models.CharField(
        verbose_name="Почта клиента",
        max_length=100,
    )

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    objects = OrderManager()

    def __str__(self):
        return self.FIO
