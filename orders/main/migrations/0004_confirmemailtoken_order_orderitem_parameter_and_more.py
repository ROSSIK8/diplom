# Generated by Django 4.2.4 on 2023-08-30 11:18

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_category_id_alter_contact_id_alter_oder_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmEmailToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='When was this token generated')),
                ('key', models.CharField(db_index=True, max_length=64, unique=True, verbose_name='Key')),
            ],
            options={
                'verbose_name': 'Токен подтверждения Email',
                'verbose_name_plural': 'Токены подтверждения Email',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(auto_now_add=True)),
                ('state', models.CharField(choices=[('basket', 'Статус корзины'), ('new', 'Новый'), ('confirmed', 'Подтвержден'), ('assembled', 'Собран'), ('sent', 'Отправлен'), ('delivered', 'Доставлен'), ('canceled', 'Отменен')], max_length=15, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Список заказ',
                'ordering': ('-dt',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Заказанная позиция',
                'verbose_name_plural': 'Список заказанных позиций',
            },
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Имя параметра',
                'verbose_name_plural': 'Список имен параметров',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='ProductParameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Параметр',
                'verbose_name_plural': 'Список параметров',
            },
        ),
        migrations.RemoveField(
            model_name='oder',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('-name',), 'verbose_name': 'Категория', 'verbose_name_plural': 'Список категорий'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-name',), 'verbose_name': 'Продукт', 'verbose_name_plural': 'Список продуктов'},
        ),
        migrations.AlterModelOptions(
            name='productinfo',
            options={'verbose_name': 'Информация о продукте', 'verbose_name_plural': 'Информационный список о продуктах'},
        ),
        migrations.AlterModelOptions(
            name='shop',
            options={'ordering': ('-name',), 'verbose_name': 'Магазин', 'verbose_name_plural': 'Список магазинов'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('email',), 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Список пользователей'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='type_user',
        ),
        migrations.AddField(
            model_name='category',
            name='shops',
            field=models.ManyToManyField(blank=True, related_name='categories', to='main.shop', verbose_name='Магазины'),
        ),
        migrations.AddField(
            model_name='contact',
            name='building',
            field=models.CharField(blank=True, max_length=15, verbose_name='Строение'),
        ),
        migrations.AddField(
            model_name='contact',
            name='structure',
            field=models.CharField(blank=True, max_length=15, verbose_name='Корпус'),
        ),
        migrations.AddField(
            model_name='productinfo',
            name='external_id',
            field=models.PositiveIntegerField(default=1, verbose_name='Внешний ИД'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productinfo',
            name='model',
            field=models.CharField(blank=True, max_length=80, verbose_name='Модель'),
        ),
        migrations.AddField(
            model_name='shop',
            name='state',
            field=models.BooleanField(default=True, verbose_name='статус получения заказов'),
        ),
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.CharField(blank=True, max_length=40, verbose_name='Компания'),
        ),
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(blank=True, max_length=40, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('shop', 'Магазин'), ('buyer', 'Покупатель')], default='buyer', max_length=5, verbose_name='Тип пользователя'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='main.category', verbose_name='Категория'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='owner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=1, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
            preserve_default=False,
        ),
        migrations.AddConstraint(
            model_name='productinfo',
            constraint=models.UniqueConstraint(fields=('product', 'shop', 'external_id'), name='unique_product_info'),
        ),
        migrations.DeleteModel(
            name='Oder',
        ),
        migrations.AddField(
            model_name='productparameter',
            name='parameter',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_parameters', to='main.parameter', verbose_name='Параметр'),
        ),
        migrations.AddField(
            model_name='productparameter',
            name='product_info',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_parameters', to='main.productinfo', verbose_name='Информация о продукте'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='ordered_items', to='main.order', verbose_name='Заказ'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product_info',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='ordered_items', to='main.productinfo', verbose_name='Информация о продукте'),
        ),
        migrations.AddField(
            model_name='order',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.contact', verbose_name='Контакт'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='confirmemailtoken',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='confirm_email_tokens', to=settings.AUTH_USER_MODEL, verbose_name='The User which is associated to this password reset token'),
        ),
        migrations.AddConstraint(
            model_name='productparameter',
            constraint=models.UniqueConstraint(fields=('product_info', 'parameter'), name='unique_product_parameter'),
        ),
        migrations.AddConstraint(
            model_name='orderitem',
            constraint=models.UniqueConstraint(fields=('order_id', 'product_info'), name='unique_order_item'),
        ),
    ]
