# Generated by Django 4.2.11 on 2024-12-20 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_number_alter_order_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='number',
            field=models.IntegerField(verbose_name='Номер клиента'),
        ),
    ]
