# Generated by Django 2.2.6 on 2019-10-06 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_sales_app', '0005_auto_20191006_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_marital_status',
            field=models.BooleanField(default=True, verbose_name='Married'),
        ),
    ]
