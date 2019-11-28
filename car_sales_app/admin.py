from django.contrib import admin
from car_sales_app.models import Customer,Sales

class  SalesAdmin(admin.ModelAdmin):
    search_fields = ['sales_id','customer__customer_id']
    list_filter = ['power_steering','airbags','sunroof','matt_finish','music_system']
    list_display = ['sales_id','purchased_date','customer','power_steering','airbags','sunroof','matt_finish','music_system']

class  CustomerAdmin(admin.ModelAdmin):
    search_fields = ['customer_id']
    list_filter = ['customer_gender','customer_region','customer_marital_status','customer_income_group']
    list_display = ['customer_id','customer_gender','customer_region','customer_marital_status','customer_income_group']

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Sales,SalesAdmin)
# Register your models here.
