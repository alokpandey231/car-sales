# Generated by Django 2.2.6 on 2019-10-06 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_sales_app', '0006_auto_20191006_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale', to='car_sales_app.Customer', verbose_name='Customer'),
        ),
    ]
