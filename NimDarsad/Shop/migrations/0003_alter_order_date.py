# Generated by Django 5.1.2 on 2024-11-27 13:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_alter_order_date_alter_product_star'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 11, 27, 17, 12, 19, 743563)),
        ),
    ]
