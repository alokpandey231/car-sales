# Generated by Django 2.2.6 on 2019-10-06 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_sales_app', '0003_auto_20191005_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=12, verbose_name='Customer gender'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_income_group',
            field=models.CharField(choices=[('0- $25K', '0- $25K'), ('$25-$70K', '$25-$70K'), ('>$70K', '>$70K')], max_length=12, verbose_name='Customer income group'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_region',
            field=models.CharField(choices=[('North', 'North'), ('South', 'South'), ('East', 'East'), ('West', 'West')], max_length=12, verbose_name='Customer region'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='fuel',
            field=models.CharField(choices=[('CNG', 'CNG'), ('Diesel', 'Diesel'), ('Petrol', 'Petrol')], max_length=12, verbose_name='Fuel'),
        ),
    ]