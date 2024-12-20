# Generated by Django 4.2.11 on 2024-12-20 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default=1, max_length=100, verbose_name='Адрес доставки'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='deadline',
            field=models.CharField(default=1, max_length=10, verbose_name='Дата доставки'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(default=1, max_length=100, verbose_name='Почта клиента'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='organization',
            field=models.CharField(default=1, max_length=100, verbose_name='Название организации'),
            preserve_default=False,
        ),
    ]