# Generated by Django 4.2.4 on 2023-10-31 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_remove_order_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='state',
        ),
    ]
