# Generated by Django 5.1.2 on 2024-11-29 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0016_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 11, 29, 18, 19, 43, 864661)),
        ),
    ]
