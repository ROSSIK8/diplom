# Generated by Django 4.2.4 on 2023-10-06 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_alter_emailconfirmation_code'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Basket',
            new_name='ListOrders',
        ),
    ]
