from django.db import models
import datetime
from django.urls import reverse
from django.utils import timezone
from decimal import Decimal
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Customer(models.Model):
    # Choices
    GENDER_CHOICE = [('Male','Male'),('Female','Female')]
    INCOME_GROUP_CHOICE = [('0- $25K','0- $25K'),('$25-$70K','$25-$70K'),('>$70K','>$70K')]
    REGION_CHOICE = [('North','North'),('South','South'),('East','East'),('West','West')]

    customer_id = models.PositiveIntegerField(verbose_name='Customer id', blank=False,unique=True)
    customer_gender  = models.CharField(verbose_name='Customer gender',max_length=12,choices = GENDER_CHOICE,blank=False)
    customer_income_group = models.CharField(verbose_name='Customer income group',max_length=12,choices = INCOME_GROUP_CHOICE,blank=False)
    customer_region = models.CharField(verbose_name='Customer region',max_length=12,choices = REGION_CHOICE,blank=False)
    customer_marital_status = models.BooleanField(verbose_name='Married',default=True)

    class Meta:
        ordering = ['customer_id']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('car_sales_app:customer_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return str(self.customer_id)

class Sales(models.Model):
    #choices
    def increment_booking_number():
        last_sales_id = Sales.objects.all().order_by('sales_id').last()
        if not last_sales_id:
            return 1
        else:
            return int(last_sales_id.sales_id) + 1

    FUEL_CHOICE = [('CNG','CNG'),('Diesel','Diesel'),('Petrol','Petrol')]

    SEGMENT_CHOICE = [('A','A'),('B','B'),('C','C')]
    sales_id = models.PositiveIntegerField(verbose_name='Sales id',blank=False,default=increment_booking_number,unique=True)
    purchased_date = models.DateField(verbose_name='Purchased date',blank=False,default=timezone.now)
    customer = models.ForeignKey(Customer,verbose_name='Customer',blank=False,on_delete=models.CASCADE,related_name='sale')
    fuel = models.CharField(verbose_name='Fuel',max_length=12,choices = FUEL_CHOICE,blank=False)
    vehicle_segment = models.CharField(verbose_name='Vehicle segment',max_length=12,choices = SEGMENT_CHOICE,blank=False)
    selling_price = models.DecimalField(verbose_name='Selling price',max_digits=18,decimal_places=2,validators=[MinValueValidator(Decimal('0.01')),MaxValueValidator(Decimal('1000000.00'))],blank=False)
    power_steering = models.BooleanField(verbose_name='Power steering',default=True)
    airbags = models.BooleanField(verbose_name='Airbags',default=True)
    sunroof = models.BooleanField(verbose_name='Sunroof',default=True)
    matt_finish = models.BooleanField(verbose_name='Matt finish',default=True)
    music_system = models.BooleanField(verbose_name='Music system',default=True)

    class Meta:
        ordering = ['sales_id']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('car_sales_app:sales_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return str(self.sales_id)
