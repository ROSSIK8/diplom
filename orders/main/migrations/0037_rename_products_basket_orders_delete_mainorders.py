# Generated by Django 4.2.4 on 2023-10-07 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_remove_basket_orders_basket_products_mainorders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basket',
            old_name='products',
            new_name='orders',
        ),
        migrations.DeleteModel(
            name='MainOrders',
        ),
    ]