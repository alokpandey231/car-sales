"""car_sales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from car_sales_app import views
from django.contrib.auth import views as auth_views
app_name = 'car_sales_app'
urlpatterns = [

    path('customer/',views.CustomerListView.as_view(),name='customer_list'),
    path('customer/<int:pk>/',views.CustomerDetailView.as_view(),name='customer_detail'),
    path('customer/create/',views.CustomerCreateView.as_view(),name='customer_create'),
    path('customer/update/<int:pk>/',views.CustomerUpdateView.as_view(),name='customer_update'),
    path('customer/delete/<int:pk>/',views.CustomerDeleteView.as_view(),name='customer_delete'),
    path('sales/',views.SalesListView.as_view(),name='sales_list'),
    path('sales/<int:pk>/',views.SalesDetailView.as_view(),name='sales_detail'),
    path('sales/create/',views.SalesCreateView.as_view(),name='sales_create'),
    path('sales/update/<int:pk>/',views.SalesUpdateView.as_view(),name='sales_update'),
    path('sales/delete/<int:pk>/',views.SalesDeleteView.as_view(),name='sales_delete'),
    path('search/',views.get_search_result,name='search_results'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('register/',views.register,name='user_register'),
    path('sales_view/',views.sales_view,name='sales_view'),

]
